import tweepy

from twitter_extraction.settings import TWITTER_CREDENTIALS
from twitter_extraction.database.mongo_connection import get_db_connection
from twitter_extraction.models.tweet import Tweet

auth = tweepy.OAuthHandler(TWITTER_CREDENTIALS['consumer_key'], TWITTER_CREDENTIALS['consumer_secret'])
auth.set_access_token(TWITTER_CREDENTIALS['access_token'], TWITTER_CREDENTIALS['secret_access_token'])


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, mongodb, api=None):
        super().__init__(api)
        self.mongodb = mongodb

    def on_status(self, status):
        self.mongodb.insert_tweet(status)
        print(vars(Tweet(status)))


stream = tweepy.Stream(auth, CustomStreamListener(get_db_connection()))

stream.filter(track=['Olympic Games'], languages=['en', 'br'])
