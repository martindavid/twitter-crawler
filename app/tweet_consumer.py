import time
from app.messaging import Messaging
from app.logger import LOG as log
from app.tweet_store import TweetStore


class TweetConsumer:

    def __init__(self):
        self.messaging = Messaging('tweets', port=32778)
        self.store = TweetStore('tweets', 'http://127.0.0.1:32773')

    def execute(self):
        try:
            while True:
                tweets = self.messaging.get(size=10)

                # If there's not tweets, take a 2 mins sleep
                if len(tweets) == 0:
                    log.info("Waiting for 2mins on next tweet batch")
                    time.sleep(120)

                for tweet in tweets:
                    self.store.save_tweet(tweet)
                    log.info(f"Successfully store tweet: {tweet['id_str']}")
        except Exception as e:
            log.error(e)
