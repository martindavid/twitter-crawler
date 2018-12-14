from typing import Union, Dict
from app.twitter_search import TwitterSearch
from app.twitter_stream import TwitterStreamRunner


class Crawler:

    STREAM_API = 'stream'
    SEARCH_API = 'search'

    @classmethod
    def create_crawler_instance(cls, api_type: str, config: Dict) -> Union[TwitterSearch, TwitterStreamRunner]:
        """

        """
        if api_type == cls.STREAM_API:
            return TwitterStreamRunner(config)

        if api_type == cls.SEARCH_API:
            return TwitterSearch(config)
