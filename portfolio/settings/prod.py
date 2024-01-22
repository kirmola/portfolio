from portfolio.settings_base import *
from os import environ

DEBUG = False


INSTALLED_APPS+=[


]

MIDDLEWARE+=[

    
]


DATABASES = {}

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# NPM_BIN_PATH = ""

ROOT_URLCONF = 'portfolio.urls'

STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
DEBUG_PROPAGATE_EXCEPTIONS = True