import factory
from ..models import TwitterUser, Tweet


class UserFactory(factory.Factory):
    FACTORY_FOR = TwitterUser

    username = factory.Sequence(lambda n: 'twitter_username_%s' % n)
    avatar_url = ''
    feeds = '1,2,3'


class TweetFactory(factory.Factory):
    FACTORY_FOR = Tweet

    user = factory.SubFactory(UserFactory)
    tweet_id = 0
    text = 'a tweet'
