from typing import Optional

from sqlmodel import SQLModel, Field


class OrderItem(SQLModel, table=True):
    __tablename__ = "order_items"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    order_id: int = Field(
        foreign_key="orders.id"
    )

    product_id: int = Field(
        foreign_key="products.id"
    )

    quantity: int

    price: float