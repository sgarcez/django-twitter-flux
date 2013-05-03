Django Twitter Flux
=============

A small Django app to persist the last X number of tweets from a set of twitter accounts. These accounts can be mapped to configurable `feeds` which are basically aggregators so you can have a timelines with multiple users and manage everything via the Admin.


* Setup:
    * requires python-twitter
	* Install dependencies with `pip install -r requirements.txt`
	* Add `twitterflux` to your INSTALLED_APPS
    * Run `syncdb`
    * Add some twitter accounts in your Admin
    * Run the management command on a cron tab: `./manage.py retrieve_tweets [-v 2]`
	* test-suite requires factory_boy
