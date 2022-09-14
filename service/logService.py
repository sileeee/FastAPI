from starlette.responses import Response

from web.repository.logRepository import LogRepository


def find_log_by_user_id(user_id: str):
    log_repo = LogRepository()
    log = log_repo.find_log_by_user_id(user_id=user_id)
    return log
