from fastapi import APIRouter
from starlette.responses import Response

from web.service import logService

router = APIRouter()


@router.get("/log/{user_id}", status_code=200) 
async def get_log_by_user_id(user_id: str):
    """
    user_id 입력으로 받아 해당 로그를 조회하는 API
    """
    log = logService.find_log_by_user_id(user_id)
    return Response(f"{log}")