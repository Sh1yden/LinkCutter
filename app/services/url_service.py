from sqlalchemy import select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from app.core import get_logger
from app.database.models import URLMap
from app.services import encode_base62

_lg = get_logger()


async def create_short_url(
    db: AsyncSession,
    original_url: str,
    custom_url: str | None = None,
) -> str:

    if custom_url:
        short_url = custom_url

    else:
        res = await db.execute(text("SELECT nextval('url_maps_id_seq')"))
        next_id = res.scalar()
        short_url = encode_base62(next_id)

    new_url = URLMap(original_url=original_url, short_url=short_url)

    if not custom_url:
        new_url.id = next_id

    db.add(new_url)

    try:
        await db.commit()

        return short_url

    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Short URL already exists.",
        )
    except Exception as e:
        await db.rollback()

        _lg.critical(f"Internal error: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


async def get_url_by_usr(db: AsyncSession, short_url: str) -> str | None:
    try:
        stmt = select(URLMap.original_url).where(URLMap.short_url == short_url)
        original_url = await db.execute(stmt)

        return original_url.scalar_one_or_none()

    except Exception as e:
        _lg.critical(f"Internal error: {e}")
