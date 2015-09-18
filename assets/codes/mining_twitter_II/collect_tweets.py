#!/usr/bin/env python

# NOTES: This script requires a running MongoDB server and the following packages:
#   - TwitterAPI: https://github.com/geduldig/TwitterAPI
#   - PyMongo
#
# It also assimes that the required twitter credentials are present in the current
# environment as follows: TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN
# and TWITTER_ACCESS_TOKEN_SECRET

import os

from pymongo import MongoClient
from TwitterAPI import TwitterAPI

if __name__ == '__main__':

    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    access_token_key = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    # MongoDB should be running locally with default port and url, otherwise specify
    client = MongoClient()

    # Both collection and database will be created by PyMongo if they don't exist yet
    tweets_coll = client.tweets_db.tweets_coll

    r = api.request('statuses/filter', {'track':'#peaceday', 'language': 'en'})
    for tweet in r:
        # Exclude retweets and tweets without location
        # Retweets can be distinguished from typical Tweets by the existence of a retweeted_status attribute.
        if not tweet.get('retweeted_status') and tweet.get('geo'):
            # Set MongoDB id
            tweet['_id'] = tweet.get('id_str')
            tweets_coll.insert(tweet)
            # Show some king of progress
            print '.',
