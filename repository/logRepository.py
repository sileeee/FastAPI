from web.repository.mongoRepository import MongoRepository


class LogRepository(MongoRepository):

    def __init__(self):
        super().__init__(database_name='fastAPI', collection_name='log')

    def find_log_by_user_id(self, user_id: str):
        _logs = self.find_one({'user_id': user_id})

        if not _logs:
            return "None"
        return _logs
