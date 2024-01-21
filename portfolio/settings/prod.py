from portfolio.settings_base import *
import dj_database_url
from os import environ
from shutil import which

DEBUG = False


INSTALLED_APPS+=[


]

MIDDLEWARE+=[

    
]


DATABASES = {
    # 'default': dj_database_url.config(default=environ['DATABASE_URL'], engine='django_cockroachdb')
}

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


NPM_BIN_PATH = which("npm")

ROOT_URLCONF = 'portfolio.urls'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'