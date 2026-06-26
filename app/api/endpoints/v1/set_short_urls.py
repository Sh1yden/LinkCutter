from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core import get_db
from app.schemas import URLCreate, URLResponse
from app.services import create_short_url

router = APIRouter()


@router.post(
    "/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED
)
async def shorten_url(payload: URLCreate, db: AsyncSession = Depends(get_db)):
    short_url = await create_short_url(
        db=db,
        original_url=str(payload.original_url),
        custom_url=payload.custom_code,
    )

    return {
        "short_url": f"https://shayden.ru/linkcutter/{short_url}",
        "original_url": payload.original_url,
        "code": short_url,
    }
