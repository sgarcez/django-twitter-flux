Django Twitter Flux
=============

A small Django app to persist the last X number of tweets from a set of twitter accounts. These accounts can be mapped to configurable `feeds` which are basically aggregators so you can have a timelines with multiple users and manage everything via the Admin.


* Setup:
    * requires python-twitter
	* Install dependencies with `pip install -r requirements.txt`
	* Add `twitterflux` to your INSTALLED_APPS
	* Create a [Twitter App](https://dev.twitter.com/) and add the credential to your settings file:
	
			TWITTER_CONSUMER_KEY = "XX"
			TWITTER_CONSUMER_SECRET = "XX"
			TWITTER_ACCESS_KEY = "XX"
			TWITTER_ACCESS_SECRET = "XX"

    * Add a a choices tuple of feeds where the first element is an `int`:
    		
    		MAIN_FEED = 'Main'
			OTHER_FEED = 'Other'

			TWITTER_FEEDS = (
    			(1, MAIN_FEED),
    			(2, OTHER_FEED),
			)

    * `syncdb`
    * Add some twitter accounts in your Admin
    * Run the management command on a cron tab: `./manage.py retrieve_tweets [-v 2]`
	* Test-suite requires factory_boy
	* Sample Django App provided.

