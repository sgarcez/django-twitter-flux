Django Twitter Flux
=============

A small Django app to persist a pool of the last X number of tweets from a set of twitter accounts. These accounts can be mapped to configurable `feeds` which are basically aggregators so you can have timelines with multiple users and manage associations via the Admin.


* Setup:
    * `pip install django-twitterflux`
	* Add `twitterflux` to your INSTALLED_APPS
	* Create a [Twitter App](https://dev.twitter.com/) and add the credentials to your `settings.py`:
	
			TWITTER_CONSUMER_KEY = "XX"
			TWITTER_CONSUMER_SECRET = "XX"
			TWITTER_ACCESS_KEY = "XX"
			TWITTER_ACCESS_SECRET = "XX"

    * Add a `TWITTER_FEEDS` feeds tuple to your `settings.py` where the first element is an `int`:
    		
    		MAIN_FEED = 'Main'
			OTHER_FEED = 'Other'

			TWITTER_FEEDS = (
    			(1, MAIN_FEED),
    			(2, OTHER_FEED),
			)

    * Optionally also add `TWITTER_BUFFER_SIZE` specifying the maximum number of tweets to keep from each account at any time (default is `5`).
    * `syncdb`
    * Add some twitter accounts in your Admin, you will be able to assign them to multiple `feeds`.
    * Run the management command on a cron tab: `./manage.py retrieve_tweets [-v 2]`
    * In your views use `get_tweets` from the `twitterflux.utils` module to get list of tweets for a specific Feed, or all tweets.
    * Requires `python-twitter`
	* Test-suite requires `factory_boy` (not installed by default)
	* Sample Django App provided.
