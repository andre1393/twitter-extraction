USER_ATTRS = [
    'id', 'name', 'screen_name', 'location', 'description', 'followers_count', 'friends_count', 'listed_count',
    'favourites_count', 'statuses_count'
]

TWEET_ATTRS = ['created_at', 'truncated', 'text', 'lang']


class Tweet:
    def __init__(self, status):
        import pdb; pdb.set_trace()
        self.user = TwitterUser(status.user)
        for tweet_attr in TWEET_ATTRS:
            setattr(self, tweet_attr, getattr(status, tweet_attr))


class TwitterUser:
    def __init__(self, user):
        self.user = {}
        for user_attr in USER_ATTRS:
            setattr(self, user_attr, getattr(user, user_attr))

    def __dict__(self):
        return vars(self)
