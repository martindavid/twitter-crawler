import time
from app.messaging import Messaging
from app.logger import LOG as log
from app.tweet_store import TweetStore
from app.config_reader import Config


class TweetConsumer:

    def __init__(self, config: Config) -> None:
        self.messaging = Messaging('tweets', port=config.messaging_port)
        self.store = TweetStore('tweets', config.db_con_str)

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
