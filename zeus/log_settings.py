# coding=utf-8

import logging
import os

LOG_DIR = '/data/log/zeus/app/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d  %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'raw': {
            'format': '%(message)s'
        }
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'filelog.log'),
            'formatter': 'verbose',
        },

        'default_err': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error_logger.log'),
            'formatter': 'verbose',
        },
        'exception_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'exception_logger.log'),
            'formatter': 'raw',
        },
        'info_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'info_logger.log'),
            'formatter': 'verbose',
        },
        'auth_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'auth_logger.log'),
            'formatter': 'verbose',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30,
        },
        'sql_logger': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'sql.log'),
            'formatter': 'verbose',
        },
        'ip_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'ip.log'),
            'formatter': 'verbose',
        },
        'profile_logger': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'profiler.log'),
            'formatter': 'raw',
        },
        'operation_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'operation.log'),
            'formatter': 'raw',
        },

    },

    'loggers': {
        # 默认都交给django了
        'django': {
            'handlers': ['default'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['default_err'],
            'level': 'ERROR',
            'propagate': False,
        },
        'exception_logger': {
            'handlers': ['exception_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'info_logger': {
            'handlers': ['info_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'auth_logger': {
            'handlers': ['auth_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'err_logger': {
            "handlers": ['default_err'],
            'level': "ERROR",
            "propagate": False,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['sql_logger'],
        },
        'ip_logger': {
            'handlers': ['ip_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'profile_logger': {
            'handlers': ['profile_logger'],
            'level': 'INFO',
            'propagate': False,
        },
        'user_logger': {
             'handlers': ['user_handler'],
             'propagate': False,
             'level': 'INFO'
         },
        'operation_logger': {
             'handlers': ['operation_handler'],
             'propagate': False,
             'level': 'INFO'
         },
    }
}


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d  %(message)s',
    filename=os.path.join(LOG_DIR, 'filelog.log'),
)


