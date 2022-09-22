import json

from fastapi import APIRouter
from web.domain.SearchKeyword import SearchKeyword
from web.service import logService

router = APIRouter()


@router.post("/log", status_code=200)
async def get_log_by_keyword(keyword: SearchKeyword):
    """
    transaction_id를 입력으로 받아 해당 로그를 조회하는 API
    :return:
    """
    log = logService.get_log_by_keyword(keyword)

    log = json.dumps(log, ensure_ascii=False, indent=4)
    log = json.loads(log)

    return log
