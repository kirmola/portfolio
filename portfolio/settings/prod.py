from portfolio.settings_base import *
import dj_database_url


DEBUG = False

INSTALLED_APPS +=[

]

INSTALLED_APPS+=[


]

MIDDLEWARE+=[

    
]


DATABASES = {
    # 'default': dj_database_url.config(default=environ['DATABASE_URL'], engine='django_cockroachdb')
}

ALLOWED_HOSTS = [".vercel.app",]

NPM_BIN_PATH = "/node18/bin/npm"

ROOT_URLCONF = 'portfolio.urls'
