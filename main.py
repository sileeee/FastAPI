import uvicorn
from fastapi import FastAPI

from web.controller import logController
from web.repository.mongoRepository import MongoRepository


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = MongoRepository()
    app = FastAPI()
    
    app.include_router(logController.router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)