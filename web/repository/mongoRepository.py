from configparser import ConfigParser
from urllib.parse import quote

from pymongo import MongoClient


class MongoRepository:

    def __init__(self, conn=None, database_name=None, collection_name=None):
        self._conn = self._get_connection() if not conn else conn
        self._database_name = database_name
        self._collection_name = collection_name


    @staticmethod
    def _get_connection():
        config = ConfigParser()
        config.read('config.ini')

        try:
            username = config["DATABASE"]["username"]
            password = config["DATABASE"]["password"]
            host = config["DATABASE"]["host"]
            port = config["DATABASE"]["port"]
            database_name = config["DATABASE"]["database_name"]
            collection_name = config["DATABASE"]["collection_name"]
            option = config["DATABASE"]["option"]

        except KeyError as ke:
            print(ke, end='')
            print("environment required")
            exit(1)

        mongo_uri = "mongodb://"+ username +":" + quote(password) + "@"+ host + ":" + port + "/" + database_name + "_" + collection_name + "?" + option;
        return MongoClient(mongo_uri)

    @property
    def database(self):
        return self._conn[self._database_name]

    @property
    def collection(self):
        return self.database[self._collection_name]

    def insert_one(self, data: dict):
        if not data:
            return
        return self.collection.insert_one(data)

    def find_one(self, _filter: dict):
        if not _filter:
            return None

        return self.collection.find_one(_filter)

    def find(self, _filter: dict):
        if not _filter:
            return None

        return self.collection.find(_filter)

    def update_one(self, _filter: dict, update_data: dict):
        if not update_data:
            return

        return self.collection.update_one(_filter, update_data)