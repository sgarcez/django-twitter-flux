# Django settings for website project.

import os
# site root is the parent folder relative to this file ie the 'project/project/' dir
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database',
    }
}

DEBUG = True

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

# USE_I18N = False

# USE_L10N = False

# USE_TZ = False

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

MEDIA_URL = '/formula1/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, '../collected/static/')

STATIC_URL = '/formula1/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'xxx'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # 'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    # 'django.core.context_processors.media',
    # 'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

SITE_ID = 1

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
