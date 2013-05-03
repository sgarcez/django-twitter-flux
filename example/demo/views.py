from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from twitterflux.utils import get_tweets


def demo(request):
    context = {
        'homefeed': get_tweets(settings.HOMEPAGE_FEED, 3),
        'homefeedinterlaced': get_tweets(settings.HOMEPAGE_FEED, 3, True),
        'otherfeed': get_tweets(settings.OTHER_FEED, 5)
    }
    return render_to_response('demo.html', context,
                              context_instance=RequestContext(request))
