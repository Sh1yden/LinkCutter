from datetime import datetime

from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class URLMap(Base):
    __tablename__ = "url_maps"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )

    original_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    short_url: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id}>"
