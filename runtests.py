import sys
from django.conf import settings


def runtests():
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
                
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['twitterflux'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
