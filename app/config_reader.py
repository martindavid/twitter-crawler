from typing import Optional, Dict, List
import logging
import json
import attr

LOG = logging.getLogger(__name__)

@attr.s(auto_attribs=True)
class Token:
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str


@attr.s(auto_attribs=True)
class Config:
    keywords: List[str]
    tokens: List[Token]
    bounding_box: List[float]
    db_name: str



def read_config(file_location: str) -> Optional[Config]:
    """
    Read a configuration file in json and return as dictionary

    :return: Dictionary containing keywords and tokens
    """
    try:
        with open(file_location, 'r') as config_file:
            config = json.load(config_file)

            tokens = [Token(
                consumer_secret=token['consumer_secret'],
                consumer_key=token['consumer_key'],
                access_token=token['access_token'],
                access_token_secret=token['access_token_secret']
            ) for token in config['tokens']]

            return Config(
                keywords=config['keywords'],
                tokens=tokens,
                bounding_box=config['bounding_box'],
                db_name=config['db_name']
            )
    except Exception as e:
        LOG.error("error_while_read_config", e.args)
        return None
