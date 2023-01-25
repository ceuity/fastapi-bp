"""App setting 모듈."""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.controller import default, sample_controller


def set_cors(app: FastAPI) -> None:
    """Cors 설정"""

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["content-disposition"],
    )


def set_routers(app: FastAPI) -> None:
    """FastAPI 라우터 설정"""

    app.include_router(default.router)
    app.include_router(sample_controller.router)


def set_event_handlers(app: FastAPI) -> None:
    """FastAPI 이벤트 핸들러 설정"""

    async def startup():
        await app.container.init_resources()

    async def shutdown():
        await app.container.shutdown_resources()

    # Database 설정
    app.add_event_handler("startup", startup)
    app.add_event_handler("shutdown", shutdown)
