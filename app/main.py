from fastapi import FastAPI

from app.app_settings import set_cors, set_routers, set_event_handlers
from app.core.containers import Container
from app.core.settings import settings
from app.core.exceptions import set_exception_handler


def create_app() -> FastAPI:
    """Create the FastAPI app."""

    tags_metadata = [
        {
            "name": "기본 API",
            "description": "default",
        },
    ]
    description = """<h2>Swagger API 문서<h2/>"""

    application = FastAPI(
        title="market-place-api",
        description=description,
        version="0.0.1",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "docExpansion": "none",
        },
        openapi_url="" if settings.env == "prod" else "/openapi.json",
        openapi_tags=tags_metadata,
    )

    # Container 설정
    container = Container()
    application.container = container

    # Event Handler 등록
    set_event_handlers(application)

    # CORS 설정
    set_cors(application)

    # Router 설정
    set_routers(application)

    # Exception Handler 설정
    set_exception_handler(application)

    return application


# FastAPI application create
app = create_app()
