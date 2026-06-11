__all__ = ["v1_router"]

from fastapi import APIRouter
from .short_urls_handles import router as url_router

v1_router = APIRouter()

v1_router.include_router(url_router)
