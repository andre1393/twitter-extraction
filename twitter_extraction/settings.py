import os


TWITTER_CREDENTIALS = {
    'consumer_key': os.getenv('TWITTER_CONSUMER_KEY'),
    'consumer_secret': os.getenv('TWITTER_CONSUMER_SECRET'),
    'access_token': os.getenv('TWITTER_ACCESS_TOKEN'),
    'secret_access_token': os.getenv('TWITTER_SECRET_ACCESS_TOKEN')
}

DB_CREDENTIALS = {
    'username': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '27017')
}
