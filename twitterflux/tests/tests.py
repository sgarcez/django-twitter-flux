from django.utils import unittest
from .factories import TweetFactory, UserFactory
from .. import utils
from ..models import TwitterUser, Tweet


class CoreModelTests(unittest.TestCase):

    def setUp(self):
        self.feed1 = UserFactory(username='sgarcez')
        self.feed1.save()
        self.feed2 = UserFactory(username='mangal2', feeds='1')
        self.feed2.save()
        self.tweet1 = TweetFactory(user=self.feed1)
        self.tweet1.save()
        self.tweet2 = TweetFactory(user=self.feed2)
        self.tweet2.save()

    def tearDown(self):
        Tweet.objects.all().delete()
        TwitterUser.objects.all().delete()

    def test_relationships(self):
        self.assertEqual(self.feed1.username, 'sgarcez')
        self.assertEqual(self.feed2.username, 'mangal2')
        self.assertEqual(self.tweet1.user, self.feed1)
        self.assertEqual(self.tweet2.user, self.feed2)

    def test_categories(self):
        home_feed = 'a'
        other_feed = 'b'
        utils.TWITTER_FEEDS = (
            (1, home_feed),
            (2, other_feed),
        )

        self.assertEqual(len(utils.get_tweets()), 2)
        self.assertEqual(len(utils.get_tweets(home_feed)), 2)
        self.assertEqual(len(utils.get_tweets(other_feed)), 1)
