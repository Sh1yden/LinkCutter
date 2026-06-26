from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core import get_db

# from app.schemas import
from app.services import get_url_by_usr

router = APIRouter()


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
