import uuid6
from datetime import date, datetime
from typing import Optional

from sqlalchemy import String, Date, DateTime, func, Index, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid6.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid6.uuid7)
    email: Mapped[Optional[str]] = mapped_column(String(128), unique=True)
    password: Mapped[Optional[str]] = mapped_column(String(128))
    nickname: Mapped[str] = mapped_column(String(20), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(20))
    birth: Mapped[Optional[date]] = mapped_column(Date)
    phone: Mapped[Optional[str]] = mapped_column(String(128))
    phone_hash: Mapped[Optional[str]] = mapped_column(String(128), unique=True)
    provider: Mapped[str] = mapped_column(String(10), default="local")
    social_id: Mapped[str] = mapped_column(String(128), unique=True)

    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        # 닉네임 대소문자 중복 닉네임 방지
        Index("ix_user_nickname_lower", func.lower(nickname), unique=True),
        # 생성일 기준 정렬을 위한 일반 인덱스 설정
        Index("ix_user_created_at", created_at.desc()),
        # 회원 정보 찾기 관련 인덱싱
        Index("ix_active_user_recovery", "name", "birth", "phone_hash", postgresql_where=text("deleted_at IS NULL")),
    )
