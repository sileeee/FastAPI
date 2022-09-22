from configparser import ConfigParser
from web.repository.mongoRepository import MongoRepository


class LogRepository(MongoRepository):

    def __init__(self):

        config = ConfigParser()
        config.read('config.ini')

        try:
            database_name = config["DATABASE"]["database_name"]
            collection_name = config["DATABASE"]["collection_name"]

        except KeyError as ke:
            print(ke, end='')
            print("environment required")
            exit(1)

        super().__init__(database_name=database_name, collection_name=collection_name)

    def find_log_by_data(self, data: dict):

        _logs = self.find(data)
        return_log = []

        if not _logs:
            return "None"

        for data in list(_logs):
            data['_id'] = str(data['_id'])
            return_log.append(data)

        return return_log