from django.db import models


class TwitterUser(models.Model):
    """
    Represents a Twitter User
    """
    username = models.CharField(max_length=50)
    avatar_url = models.URLField(blank=True)
    feeds = models.CommaSeparatedIntegerField(
        max_length=255, blank=True, default='',
        help_text='Feeds are groups of user timelines.')

    def __unicode__(self):
        return self.username


class Tweet(models.Model):
    """
    Represents a Tweet
    """
    user = models.ForeignKey(TwitterUser)
    tweet_id = models.BigIntegerField()
    text = models.CharField(max_length=500)

    def __unicode__(self):
        return '%s - %s' % (self.user, self.text)

    class Meta:
        ordering = ('-tweet_id',)
