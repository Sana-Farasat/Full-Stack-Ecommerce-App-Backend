from pydantic import BaseModel

from app.schemas.product import ProductCartResponse


class CartCreate(BaseModel):
    product_id: int
    quantity: int


class CartResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

class CartResponse(BaseModel):
    id: int
    quantity: int
    product: ProductCartResponse