from .models import TwitterUser, Tweet
from .settings import TWITTER_BUFFER_SIZE, TWITTER_FEEDS


def get_tweets(category=None, per_user=1, interlaced=False):
    """returns list of tweets

    :param category: string used to fetch int from TWITTER_FEEDS
    :param per_user: number of tweets per user
    :param interlaced: wether the tweets should be returned
    interlaced(1 per account in sequence) or chronologically(default.
    :returns: list
    """
    per_user = min(per_user, TWITTER_BUFFER_SIZE)

    if category:
        try:
            cat_id = [t[0] for t in TWITTER_FEEDS if t[1] == category][0]
            users = TwitterUser.objects.filter(feeds__contains=str(cat_id))
        except IndexError:
            return None
    else:
        users = TwitterUser.objects.all()

    if interlaced:
        tweets = []
        for x in range(per_user):
            # alternating tweets for each account
            # should refactor maybe.
            for user in users:
                try:
                    tweets.append(user.tweet_set.all()[x])
                except:
                    pass
        return tweets
    else:
        return Tweet.objects.filter(user_id__in=users)
