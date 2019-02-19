import json
import time
import tweepy
from tweepy.streaming import StreamListener
from app.logger import LOG as log
# from app.sentiment_analysis import SentimentAnalysis
from app.config_reader import Config
from app.messaging import Messaging

# Get the box coordinates from http://boundingbox.klokantech.com/
AUS_GEO_CODE = [113.03, -39.06, 154.73, -12.28]


class TwitterStream(StreamListener):
    """A listener class that will listen twitter streaming data"""

    def __init__(self):
        self.tweets = 0
        self.messaging = Messaging('twitter_stream', port=32776)

    def on_data(self, data):
        """ Method to passes data from statuses to the on_status method"""
        if 'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            log.warning(warning['message'])
            return False

    def on_status(self, status):
        """ Handle logic when the data coming """
        try:
            tweet = json.loads(status)
            # Update sentiment score
            # tweet["sentiment"] = SentimentAnalysis.get_sentiment(tweet_text=tweet["text"])
            # log.info(f"Tweet - {tweet['text']}")
            self.tweets += 1
            self.messaging.publish(tweet)
            log.info(f"Count {self.tweets}")
        except Exception as e:
            log.error(e)

    def on_error(self, status):
        """ Handle any error throws from stream API """
        if status == 420:
            self.on_timeout()

    def on_timeout(self):
        """ Handle time out when API reach its limit """
        log.info("API Reach its limit, sleep for 10 minutes")
        time.sleep(600)
        return


class TwitterStreamRunner:
    """ Main class to run twitter stream listener

    Args:
        group_name: a group that used to fetch a list of keyword
    """

    def __init__(self, config: Config) -> None:
        # Set tweepy api object and authentication
        token = config.tokens[0]
        self.auth = tweepy.OAuthHandler(
            token.consumer_key, token.consumer_secret)
        self.auth.set_access_token(token.access_token, token.access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.keywords = config.keywords
        self.bounding_box = config.bounding_box

    def execute(self):
        """Execute the twitter crawler, loop into the keyword_list
        """
        listen = TwitterStream()
        stream = tweepy.Stream(self.auth, listen)
        loop = True
        while loop:
            try:
                log.info("Start stream tweets data")
                stream.filter(locations=self.bounding_box)
                loop = False
                log.info("End stream tweets data")
            except Exception as e:
                log.error("There's an error, sleep for 10 minutes")
                log.error(e)
                loop = True
                stream.disconnect()
                time.sleep(600)
                continue
