from portfolio.settings_base import *
from os import environ

DEBUG = True


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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'