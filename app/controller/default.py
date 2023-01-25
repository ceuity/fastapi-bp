from dependency_injector.wiring import inject
from fastapi import APIRouter

router = APIRouter(tags=["기본 API"])


@router.get("/health")
@inject
async def health_check():
    """Health check logic"""

    return {"result": "ok"}
