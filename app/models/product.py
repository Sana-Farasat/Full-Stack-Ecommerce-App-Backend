from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import SQLModel, Field
from sqlmodel import Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.cart import Cart

class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True)

    title: str = Field(index=True)
    slug: str = Field(unique=True, index=True)

    description: str

    price: Decimal
    discount_price: Optional[Decimal] = None

    stock: int = 0

    sku: str = Field(unique=True)

    category_id: int | None = Field(default=None, foreign_key="categories.id")

    image: Optional[str] = None

    is_active: bool = True

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    cart_items: list["Cart"] = Relationship(back_populates="product")