from datetime import datetime, UTC
from typing import Optional

from sqlmodel import SQLModel, Field


class Order(SQLModel, table=True):
    __tablename__ = "orders"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(
        foreign_key="users.id"
    )

    total_price: float

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )