from portfolio.settings_base import *
import dj_database_url
from os import environ

DEBUG = False


INSTALLED_APPS+=[


]

MIDDLEWARE+=[

    
]


DATABASES = {
    # 'default': dj_database_url.config(default=environ['DATABASE_URL'], engine='django_cockroachdb')
}

ALLOWED_HOSTS = [".onrender.com"]

RENDER_EXTERNAL_HOSTNAME = environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


NPM_BIN_PATH = ""

ROOT_URLCONF = 'portfolio.urls'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'