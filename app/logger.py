from logging.config import dictConfig
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] '
                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        },
        'sentry': {
            'format': '[%(asctime)s][%(levelname)s] '
                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },

    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'cli': {
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

dictConfig(LOGGING)
LOG = logging.getLogger(__name__)
