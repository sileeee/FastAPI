
from starlette.responses import Response

from web.domain.SearchKeyword import SearchKeyword
from web.repository.logRepository import LogRepository


def get_log_by_keyword(keyword: SearchKeyword):
    log_repo = LogRepository()

    data = dict()
    for i in keyword:
        if i[1] == None or i[1]=="":
            continue
        else:
            data[i[0]] = i[1]

    log = log_repo.find_log_by_data(data)
    return log