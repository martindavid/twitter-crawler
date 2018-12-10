from typing import Optional, Dict
import logging
import json

LOG = logging.getLogger(__name__)


def read_config(file_location: str) -> Optional[Dict]:
    """
    Read a configuration file in json and return as dictionary

    :return: Dictionary containing keywords and tokens
    """
    try:
        with open(file_location, 'r') as config_file:
            config = json.load(config_file)
            LOG.debug(config)
            return config
    except Exception as e:
        LOG.error("error_while_read_config", e.args)
        return None
