import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from web.controller import logController, mainController
from web.repository.mongoRepository import MongoRepository


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = MongoRepository()
    app = FastAPI()

    origins = [
        "http://localhost:63342",
        "http://localhost",
        "http://localhost:8080",
        "http://127.0.0.1:56736",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins, # resource 요청을 허용할 origins
        allow_credentials=True,  # cross-origin request에서 cookie를 포함할 것인지
        allow_methods=["*"],  # cross-origin reqeust에서 허용할 methos(기본값 GET)
        allow_headers=["*"],  # cross-origin request에서 허용할 HTTP Header목록
    )

    # 라우터 정의
    app.include_router(mainController.router)
    app.include_router(logController.router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)