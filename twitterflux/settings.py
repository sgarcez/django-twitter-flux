import sys
from django.conf import settings

current_module = sys.modules[__name__]

required_attrs = ('TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET',
                  'TWITTER_ACCESS_KEY', 'TWITTER_ACCESS_SECRET', 'TWITTER_FEEDS')

for r in required_attrs:
    try:
        setattr(current_module, r, getattr(settings, r))
    except AttributeError:
        raise Exception('Could not find `%s` in your django settings file' % r)

TWITTER_BUFFER_SIZE = getattr(settings, 'TWITTER_BUFFER_SIZE', 5)
