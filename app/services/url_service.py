from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from app.core import get_logger
from app.database.models import URLMap
from app.services.shortener import encode_base62

_lg = get_logger()


async def create_short_url(
    db: AsyncSession,
    original_url: str,
    custom_url: str | None = None,
) -> URLMap | None:
    try:
        if custom_url:
            stmt = select(URLMap).where(URLMap.short_url == custom_url)
            res = await db.execute(stmt)

            if res.scalar_one_or_none():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="URL already exists",
                )

            short_url = custom_url

        else:
            res = await db.execute(text("SELECT nextval('url_maps_id_seq')"))
            next_id = res.scalar()

            short_url = encode_base62(next_id)

        new_url = URLMap(original_url=original_url, short_url=short_url)

        if not custom_url:
            new_url.id = next_id

        _lg.debug(f"Short url created: {new_url}")

        db.add(new_url)
        await db.commit()
        await db.refresh(new_url)
        return new_url

    except Exception as e:
        _lg.critical(f"Internal error: {e}")


async def get_url_by_usr(db: AsyncSession, shor_url: str) -> URLMap | None:
    try:
        stmt = select(URLMap).where(URLMap.short_url == shor_url)
        res = await db.execute(stmt)

        return res.scalar_one_or_none()

    except Exception as e:
        _lg.critical(f"Internal error: {e}")
