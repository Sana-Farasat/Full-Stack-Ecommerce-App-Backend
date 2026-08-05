from sqlmodel import Session
from sqlmodel import select
from app.models.order import Order
from app.models.order_item import OrderItem


def create_order(
    session: Session,
    order: Order,
):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def create_order_item(
    session: Session,
    item: OrderItem,
):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item




def get_orders(
    session: Session,
    user_id: int,
):
    statement = (
        select(Order)
        .where(Order.user_id == user_id)
        .order_by(Order.created_at.desc())
    )

    return session.exec(statement).all()