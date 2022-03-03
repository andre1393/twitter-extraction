
import logging
from pymongo import MongoClient

from twitter_extraction.utils import Singleton
from twitter_extraction.settings import DB_CREDENTIALS

logger = logging.getLogger(__name__)


class DBConnection(metaclass=Singleton):

    def __init__(self, username, password, host, port):
        self.client = MongoClient(
            host=host,
            port=int(port),
            username=username,
            password=password,
            authSource='admin'
        )

    def _get_database(self):
        """ get database
        :return: database client object
        """
        return self.client['twitter']

    def insert_tweet(self, status):
        db = self._get_database()


def get_db_connection():
    return DBConnection(**DB_CREDENTIALS)
