import sys
from django.conf import settings

settings.configure(DEBUG=True,
               DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                    }
                },
               INSTALLED_APPS=('django.contrib.auth',
                              'django.contrib.contenttypes',
                              'django.contrib.sessions',
                              'django.contrib.admin',
                              'twitterflux',),
                TWITTER_CONSUMER_KEY = "XX",
                TWITTER_CONSUMER_SECRET = "XX",
                TWITTER_ACCESS_KEY = "XX",
                TWITTER_ACCESS_SECRET = "XX",
                TWITTER_FEEDS = ())

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['twitterflux', ])
if failures:
    sys.exit(failures)