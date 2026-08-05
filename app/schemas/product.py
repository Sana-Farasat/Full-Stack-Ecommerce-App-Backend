from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class ProductCreate(BaseModel):
    title: str
    slug: str
    description: str
    price: Decimal
    discount_price: Optional[Decimal] = None
    stock: int
    sku: str
    image: Optional[str] = None
    category_id: int | None = None


class ProductResponse(BaseModel):
    id: int
    title: str
    slug: str
    description: str
    price: Decimal
    discount_price: Optional[Decimal]
    stock: int
    sku: str
    image: Optional[str]
    category_id: int | None

class ProductUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: Decimal | None = None
    discount_price: Decimal | None = None
    stock: int | None = None
    image: str | None = None
    category_id: int | None = None

class ProductCartResponse(BaseModel):
    id: int
    title: str
    price: float
    image: str | None = None