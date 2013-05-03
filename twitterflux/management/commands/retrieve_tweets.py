from optparse import make_option
import twitter
from django.core.management.base import BaseCommand, CommandError
from ...models import TwitterUser, Tweet
from ...settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,\
    TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET, TWITTER_BUFFER_SIZE


class Command(BaseCommand):

    if '--verbosity' not in [opt.get_opt_string() for opt in BaseCommand.option_list]:
        option_list = BaseCommand.option_list + (
            make_option('--verbosity', action='store', dest='verbosity', default='1',
                        type='choice', choices=['0', '1', '2'],
                        help='Verbosity level; 0=minimal output, 1=normal output, 2=all output'),
        )
    help = 'Retrieve batch of tweets for all users.'

    def handle(self, **options):
        verbosity = int(options.get('verbosity', 0))

        api = twitter.Api(
            consumer_key=TWITTER_CONSUMER_KEY,
            consumer_secret=TWITTER_CONSUMER_SECRET,
            access_token_key=TWITTER_ACCESS_KEY,
            access_token_secret=TWITTER_ACCESS_SECRET)

        try:
            api.VerifyCredentials()
        except twitter.TwitterError:
            raise CommandError('Could not authenticate with Twitter using the credentials provided.')

        users = TwitterUser.objects.all()
        for feed in users:
            if verbosity > 0:
                print '=' * 60
                print 'Retrieving tweets for feed: %s' % feed

            try:
                last = Tweet.objects.filter(user=feed).order_by('-tweet_id')[:1].get()
                last_id = last.tweet_id
                if verbosity > 1:
                    print 'Last stored tweet: %s' % last.text
            except Tweet.DoesNotExist:
                last_id = None
                if verbosity > 1:
                    print 'No previous tweets for feed.'

            try:
                statuses = api.GetUserTimeline(feed, since_id=last_id, exclude_replies=True)[:TWITTER_BUFFER_SIZE]
                # not using `count` api parameter because it return irregular number of tweets
                # when used with the exclude_replies option.
                # with the slice we are guaranteed to receice `buffer_size` number of tweets.
            except twitter.TwitterError:
                raise CommandError('Could not retrieve the Twitter Timeline for feed: `%s`' % feed)

            if statuses:
                if statuses[0].user.profile_image_url != feed.avatar_url:
                        feed.avatar_url = statuses[0].user.profile_image_url
                        feed.save()
                        if verbosity > 1:
                            print 'Updated avatar'

                for s in statuses:
                    t = Tweet(user=feed, text=s.text, tweet_id=int(s.id))
                    t.save()
                    if verbosity > 1:
                        print 'Stored tweet: %s' % s.text

            if verbosity > 0:
                print 'Removing stale tweets'
            old_tweets = Tweet.objects.filter(user=feed).order_by('-tweet_id')[TWITTER_BUFFER_SIZE:]
            for old in old_tweets:
                old.delete()
                if verbosity > 1:
                    print 'Deleted tweet: %s' % old.text
