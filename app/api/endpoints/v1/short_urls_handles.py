from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.core import get_db
from app.schemas import URLCreate, URLResponse
from app.services import url_service

router = APIRouter()


@router.post(
    "/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED
)
async def shorten_url(payload: URLCreate, db: AsyncSession = Depends(get_db)):
    return await url_service.create_short_url(
        db=db,
        original_url=str(payload.original_url),
        custom_url=payload.custom_code,
    )


@router.get("/{short_url}")
async def redirect_to_original(short_url: str, db: AsyncSession = Depends(get_db)):
    url_map = await url_service.get_url_by_usr(db, short_url)

    if not url_map:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found."
        )

    return RedirectResponse(
        url=url_map.original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )
