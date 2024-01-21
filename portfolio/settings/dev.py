from portfolio.settings_base import *
from os import name as os_name


DEBUG = True

INSTALLED_APPS+=[
    'django_browser_reload',
    
]

MIDDLEWARE+=[
    "django_browser_reload.middleware.BrowserReloadMiddleware",

    
]

DATABASES = {}

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

if os_name == "nt":
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
else:
    NPM_BIN_PATH = "/node18/bin/npm"


ROOT_URLCONF = 'portfolio.urls_dev'
