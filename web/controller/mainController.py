import os

from fastapi import APIRouter
from starlette.responses import Response

root = os.path.dirname(os.path.abspath("web/view/main.html"))
router = APIRouter()


@router.get("/") #, response_class=HTMLResponse
async def main():
    with open(os.path.join(root, 'main.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")
