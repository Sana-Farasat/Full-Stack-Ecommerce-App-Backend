from sqlmodel import Session, select
from app.models.cart import Cart
from sqlalchemy.orm import selectinload

# def get_cart_item(session: Session, user_id: int, product_id: int):
#     statement = select(Cart).where(
#         Cart.user_id == user_id,
#         Cart.product_id == product_id,
#     )
#     return session.exec(statement).first()
def get_cart_item(
    session: Session,
    user_id: int,
    product_id: int,
):
    statement = (
        select(Cart)
        .options(
            selectinload(Cart.product)
        )
        .where(
            Cart.user_id == user_id,
            Cart.product_id == product_id,
        )
    )

    return session.exec(statement).first()

def add_to_cart(session: Session, cart: Cart):
    session.add(cart)
    session.commit()
    session.refresh(cart)
    return cart


def update_cart(session: Session, cart: Cart):
    session.add(cart)
    session.commit()
    session.refresh(cart)
    return cart


# def get_cart(session: Session, user_id: int):
#     statement = select(Cart).where(
#         Cart.user_id == user_id
#     )
#     return session.exec(statement).all()
def get_cart(session: Session, user_id: int):
    statement = (
        select(Cart)
        .options(
            selectinload(Cart.product)
        )
        .where(
            Cart.user_id == user_id
        )
    )

    return session.exec(statement).all()

# def get_cart_by_id(session: Session, cart_id: int):
#     return session.get(Cart, cart_id)
def get_cart_by_id(
    session: Session,
    cart_id: int,
):
    statement = (
        select(Cart)
        .options(
            selectinload(Cart.product)
        )
        .where(
            Cart.id == cart_id
        )
    )

    return session.exec(statement).first()

def remove_cart_item(session: Session, cart: Cart):
    session.delete(cart)
    session.commit()

def clear_cart(session: Session, user_id: int):
    items = get_cart(session, user_id)

    for item in items:
        session.delete(item)

    session.commit()