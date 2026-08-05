from typing import Optional

from sqlmodel import SQLModel, Field

from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.user import User

class Cart(SQLModel, table=True):
    __tablename__ = "cart"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="users.id")

    product_id: int = Field(foreign_key="products.id")

    quantity: int = 1

    user: "User" = Relationship()

    product: "Product" = Relationship(
        back_populates="cart_items"
)