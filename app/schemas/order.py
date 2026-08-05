from datetime import datetime
from pydantic import BaseModel


class OrderResponse(BaseModel):
    id: int
    total_price: float
    created_at: datetime