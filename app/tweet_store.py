import couchdb
import json
from app.logger import LOG as log

DEFAULT_URL = 'http://127.0.0.1:5984/'

class TweetStore(object):
    """ Main class to handle interaction with CouchDB database

    Args:
        db_name: database name in couchdb
        url: connection url for couchdb, by default 'http://127.0.0.1:5984/'

    Attributes:
        server: couchdb server instance
        dbase: database instance of couchdb server
    """

    def __init__(self, db_name, url=DEFAULT_URL):
        try:
            self.server = couchdb.Server(url=url)
            self.server.login("admin","password")
            self.dbase = self.server.create(db_name)
        except couchdb.http.PreconditionFailed:
            self.dbase = self.server[db_name]


    def save_tweet(self, twitter):
        """Save tweet data into database
        Will check if data is not exists then save it, if exists ignore it

        Args:
            twitter: tweepy status object
        """
        if isinstance(twitter, dict):
            json_data = twitter
        else:
            json_data = json.loads(twitter)

        parsed_tweet = self.parse_tweet(json_data)
        doc = self.dbase.get(parsed_tweet["id"])
        if doc is None:
            try:
                self.dbase.save(parsed_tweet)
            except Exception as e:
                log.error(e)


    def parse_tweet(self, json_data):
        tweet = {
            "id": json_data.get("id_str"),
            "created_at": json_data.get("created_at"),
            "source": json_data.get("source"),
            "text": json_data.get("text"),
            "lang": json_data.get("lang"),
            "entities": json_data.get("entities"),
            "coordinates": json_data.get("coordinates"),
            "places": json_data.get("places")
        }

        if json_data.get("extended_tweet"):
            tweet["long_text"] = json_data.get("extended_tweet").get("full_text")

        if json_data.get("user"):
            tweet["user"] = self.parse_user_object(json_data.get("user"))

        return tweet


    def parse_user_object(self, user_data):
        return {
            "id": user_data.get("id_str"),
            "name": user_data.get("name"),
            "screen_name": user_data.get("screen_name"),
            "location": user_data.get("location"),
            "description": user_data.get("description"),
            "followers_count": user_data.get("followers_count"),
            "friends_count": user_data.get("friends_count"),
            "profile_image": user_data.get("profile_image_url_https")
        }

