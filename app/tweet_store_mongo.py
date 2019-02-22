import json
from pymongo import MongoClient
from app.logger import LOG as log


class TweetStore(object):
    """ Main class to handle interaction with data store (mongodb)

    Args:
        db_name: database
        url: connection url for mongodb, by default 'http://127.0.0.1:27017/'

    Attributes:
        server: couchdb server instance
        dbase: database instance of couchdb server
    """

    def __init__(self, db_name: str, host: str = 'localhost', port: int = 27017) -> None:
        client = MongoClient(host, port)
        self.db = client[db_name]
        self.tweets = self.db.tweets


    def save_tweet(self, twitter) -> None:
        """Save tweet data into database
        Will check if data is not exists then save it, if exists ignore it

        Args:
            twitter: tweepy status object
        """
        if isinstance(twitter, dict):
            json_data = twitter
        else:
            json_data = json.loads(twitter)

        try:
            breakpoint()
            self.db.tweets.find_one_and_update(
                {'id_str': json_data['id_str']},
                {'$inc': {'seq': 1}},
                projection={'seq': True, '_id': False},
                upsert=True,
            )
        except Exception as e:
            log.error(e)
