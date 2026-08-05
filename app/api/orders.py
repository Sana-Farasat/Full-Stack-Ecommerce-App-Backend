from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.dependencies.auth import get_current_user

from app.models.user import User
from app.models.order import Order
from app.models.order_item import OrderItem

from app.schemas.order import OrderResponse

from app.crud.cart import (
    get_cart,
    clear_cart,
)

from app.crud.order import (
    create_order,
    create_order_item,
)

from app.crud.order import (
    create_order,
    create_order_item,
    get_orders,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post("/checkout", response_model=OrderResponse)
def checkout(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    cart_items = get_cart(
        session,
        current_user.id,
    )

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    order = Order(
        user_id=current_user.id,
        total_price=total,
    )

    order = create_order(
        session,
        order,
    )

    for item in cart_items:
        create_order_item(
            session,
            OrderItem(
                order_id=order.id,
                product_id=item.product.id,
                quantity=item.quantity,
                price=item.product.price,
            ),
        )

    clear_cart(
        session,
        current_user.id,
    )

    return order

@router.get("/", response_model=list[OrderResponse])
def list_orders(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return get_orders(
        session,
        current_user.id,
    )