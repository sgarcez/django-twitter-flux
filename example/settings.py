DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database',
    }
}

DEBUG = True

STATIC_URL = '/static/'

SECRET_KEY = 'xxx'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'demo',
    'twitterflux',
)


HOMEPAGE_FEED = 'Homepage'
OTHER_FEED = 'Other Page'

TWITTER_FEEDS = (
    (1, HOMEPAGE_FEED),
    (2, OTHER_FEED),
)
TWITTER_CONSUMER_KEY = "XX"
TWITTER_CONSUMER_SECRET = "XX"
TWITTER_ACCESS_KEY = "XX"
TWITTER_ACCESS_SECRET = "XX"
