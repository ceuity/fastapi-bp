import json

from fastapi import FastAPI
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException

from app.core.log import logger


class ApiError(Exception):
    """Api error base exception class"""

    def __init__(self, code: int, name: str = "BadRequest"):
        """Api exception용 생성자"""
        self.code = code
        self.name = name

    def to_response(self):
        """Response 변환"""
        return JSONResponse(
            status_code=self.code,
            content={"message": f"[{self.name}] check your request."},
        )


class BadRequest(ApiError):
    """Resource not found exception"""

    def __init__(self, name: str = "BadRequest"):
        """Constructor with name"""
        self.name = name


class UnauthorizedError(ApiError):
    """Unauthorized exception"""

    def __init__(self, name: str = "UnauthorizedError"):
        """Constructor with name"""
        self.name = name


class ResourceNotFound(ApiError):
    """Resource not found exception"""

    def __init__(self, name: str = "Resource"):
        """Constructor with name"""
        self.name = name


class InternalServerError(ApiError):
    """Api Error exception"""

    def __init__(self, name: str = "InternalServerError"):
        """Constructor with name"""
        self.name = name


def set_exception_handler(app: FastAPI) -> None:
    """Exception handler 설정

     익셉션 발생시 해당 예외들을 미리 등록하여 사용한다.
     예) raise ResourceNotFound()

    Args:
        app (FastAPI): FastAPI application 객체

    """

    @app.exception_handler(BadRequest)
    async def bad_request_handler(request: Request, exc: BadRequest):
        logger.info(f"BadRequest {request.headers}")
        return JSONResponse(
            status_code=400,
            content={"message": f"{exc.name}"},
        )

    @app.exception_handler(UnauthorizedError)
    async def unauthorized_error_handler(request: Request, exc: UnauthorizedError):
        logger.info(f"UnauthorizedError {request.headers}")
        return JSONResponse(
            status_code=401,
            content={"message": f"{exc.name}"},
        )

    @app.exception_handler(ResourceNotFound)
    async def resource_exception_handler(request: Request, exc: ResourceNotFound):
        logger.info(f"ResourceNotFound {request.headers}")
        return JSONResponse(
            status_code=404,
            content={"message": f"{exc.name} not Found."},
        )

    @app.exception_handler(ValidationError)
    async def validation_error_handler(request: Request, exc: ValidationError):
        logger.info(f"ValidationError {request.headers}")
        return JSONResponse(
            status_code=422,
            content=json.loads(exc.json()),
        )

    @app.exception_handler(InternalServerError)
    async def internal_error_handler(request: Request, exc: InternalServerError):
        logger.info(f"InternalServerError {request.headers}")
        return JSONResponse(
            status_code=500,
            content={"message": f"{exc.name}"},
        )

    @app.exception_handler(404)
    async def custom_404_handler(request: Request, exc: HTTPException):
        logger.info(f"Custom 404 Handler {request.headers} {exc}")
        return JSONResponse(
            status_code=404,
            content={"message": "Resource not found"},
        )

    @app.exception_handler(500)
    async def custom_500_handler(request: Request, exc: HTTPException):
        logger.info(f"Custom 500 Handler {request.headers} {exc}")
        return JSONResponse(
            status_code=500,
            content={"message": "Internal server error"},
        )
