from logging.config import dictConfig
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

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
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': 'https://14d9c02ed94d46789b6d9ab95aa28cde@sentry.io/158861',
            'enable_breadcrumbs': False
        },
    },

    'loggers': {
        '': {
            'handlers': ['console', 'sentry'],
            'level': 'DEBUG',
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
