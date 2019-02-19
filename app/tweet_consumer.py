from app.messaging import Messaging
from app.logger import LOG as log
import time


class TweetConsumer:

    def __init__(self):
        self.messaging = Messaging('twitter_stream', port=32776)


    def execute(self):
        try:
            while True:
                tweets = self.messaging.get(size=10)

                # If there's not tweets, take a 2 mins sleep
                if len(tweets) == 0:
                    log.info("Waiting for 2mins on next tweet batch")
                    time.sleep(120)

                for tweet in tweets:
                    log.info(tweet)
        except Exception as e:
            log.error(e)

