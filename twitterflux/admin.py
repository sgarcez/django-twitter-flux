from django import forms
from django.contrib import admin
from django.forms.widgets import CheckboxSelectMultiple
from .models import TwitterUser, Tweet
from .settings import TWITTER_FEEDS


# Widget
class CSICheckboxSelectMultiple(CheckboxSelectMultiple):
    def value_from_datadict(self, data, files, name):
        return ','.join(data.getlist(name))

    def render(self, name, value, attrs=None, choices=()):
        if value:
            value = value.split(',')
        return super(CSICheckboxSelectMultiple, self).render(
            name, value, attrs=attrs, choices=choices
        )


# Form field
class CSIMultipleChoiceField(forms.MultipleChoiceField):
    widget = CSICheckboxSelectMultiple

    def to_python(self, value):
        return value

    def validate(self, value):
        if value:
            value = value.split(',')
        super(CSIMultipleChoiceField, self).validate(value)


class TwitterUserAdminForm(forms.ModelForm):
    feeds = CSIMultipleChoiceField(
        required=False, choices=TWITTER_FEEDS
    )

    class Meta:
        model = TwitterUser


class TwitterUserAdmin(admin.ModelAdmin):
    form = TwitterUserAdminForm
    exclude = ['avatar_url']


class TweetAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    readonly_fields = ('user', 'tweet_id', 'text')

    def has_add_permission(self, request):
            return False

admin.site.register(TwitterUser, TwitterUserAdmin)
admin.site.register(Tweet, TweetAdmin)
