from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core import get_db
from app.schemas import URLCreate, URLResponse
from app.services import create_short_url, get_url_by_usr

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


@router.get("/{short_url}")
async def redirect(short_url: str, db: AsyncSession = Depends(get_db)):
    target_url = await get_url_by_usr(db, short_url)

    if not target_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found."
        )

    return RedirectResponse(
        url=target_url,
        status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    )
