from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True, unique=True)
    slug: str = Field(index=True, unique=True)

    image: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)