# from fastapi import APIRouter, Depends, HTTPException
# from sqlmodel import Session

# from app.db.session import get_session
# from app.dependencies.auth import get_current_user

# from app.models.cart import Cart
# from app.models.user import User

# from app.schemas.cart import CartCreate, CartResponse

# from app.crud.cart import (
#     add_to_cart,
#     clear_cart,
#     get_cart,
#     get_cart_by_id,
#     get_cart_item,
#     remove_cart_item,
#     update_cart,
# )

# router = APIRouter(
#     prefix="/cart",
#     tags=["Cart"],
# )

# @router.post("/", response_model=CartResponse)
# def create_cart(
#     data: CartCreate,
#     session: Session = Depends(get_session),
#     current_user: User = Depends(get_current_user),
# ):
#     item = get_cart_item(
#         session,
#         current_user.id,
#         data.product_id,
#     )

#     if item:
#         item.quantity += data.quantity
#         return update_cart(session, item)

#     cart = Cart(
#         user_id=current_user.id,
#         product_id=data.product_id,
#         quantity=data.quantity,
#     )

#     # return add_to_cart(session, cart)
#     cart = add_to_cart(session, cart)

#     return CartResponse(
#         id=cart.id,
#         quantity=cart.quantity,
#         product={
#             "id": cart.product.id,
#             "title": cart.product.title,
#             "price": cart.product.price,
#             "image": cart.product.image,
#         },
# )

# @router.get("/", response_model=list[CartResponse])
# def list_cart(
#     session: Session = Depends(get_session),
#     current_user: User = Depends(get_current_user),
# ):
#     return get_cart(
#         session,
#         current_user.id,
#     )

# @router.patch("/{cart_id}", response_model=CartResponse)
# def update_cart_quantity(
#     cart_id: int,
#     quantity: int,
#     session: Session = Depends(get_session),
#     current_user: User = Depends(get_current_user),
# ):
#     cart = get_cart_by_id(session, cart_id)

#     if not cart:
#         raise HTTPException(404, "Cart item not found")

#     if cart.user_id != current_user.id:
#         raise HTTPException(403, "Forbidden")

#     cart.quantity = quantity

#     return update_cart(session, cart)

# @router.delete("/{cart_id}")
# def delete_cart_item(
#     cart_id: int,
#     session: Session = Depends(get_session),
#     current_user: User = Depends(get_current_user),
# ):
#     cart = get_cart_by_id(session, cart_id)

#     if not cart:
#         raise HTTPException(404, "Cart item not found")

#     if cart.user_id != current_user.id:
#         raise HTTPException(403, "Forbidden")

#     remove_cart_item(session, cart)

#     return {
#         "message": "Item removed"
#     }

# @router.delete("/")
# def delete_cart(
#     session: Session = Depends(get_session),
#     current_user: User = Depends(get_current_user),
# ):
#     clear_cart(
#         session,
#         current_user.id,
#     )

#     return {
#         "message": "Cart cleared"
#     }

# @router.get("/", response_model=list[CartResponse])
# def list_cart(
#     session: Session = Depends(get_session),
#     current_user: User = Depends(get_current_user),
# ):
#     items = get_cart(
#         session,
#         current_user.id,
#     )

#     response = []

#     for item in items:
#         response.append(
#             CartResponse(
#                 id=item.id,
#                 quantity=item.quantity,
#                 product={
#                     "id": item.product.id,
#                     "title": item.product.title,
#                     "price": item.product.price,
#                     "image": item.product.image,
#                 },
#             )
#         )

#     return response

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.db.session import get_session
from app.dependencies.auth import get_current_user

from app.models.cart import Cart
from app.models.user import User

from app.schemas.cart import CartCreate, CartResponse

from app.crud.cart import (
    add_to_cart,
    clear_cart,
    get_cart,
    get_cart_by_id,
    get_cart_item,
    remove_cart_item,
    update_cart,
)

router = APIRouter(
    prefix="/cart",
    tags=["Cart"],
)


@router.post("/", response_model=CartResponse)
def create_cart(
    data: CartCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    item = get_cart_item(
        session,
        current_user.id,
        data.product_id,
    )

    if item:
        item.quantity += data.quantity
        item = update_cart(session, item)

        return CartResponse(
            id=item.id,
            quantity=item.quantity,
            product={
                "id": item.product.id,
                "title": item.product.title,
                "price": item.product.price,
                "image": item.product.image,
            },
        )

    cart = Cart(
        user_id=current_user.id,
        product_id=data.product_id,
        quantity=data.quantity,
    )

    cart = add_to_cart(session, cart)

    return CartResponse(
        id=cart.id,
        quantity=cart.quantity,
        product={
            "id": cart.product.id,
            "title": cart.product.title,
            "price": cart.product.price,
            "image": cart.product.image,
        },
    )


@router.get("/", response_model=list[CartResponse])
def list_cart(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    items = get_cart(
        session,
        current_user.id,
    )

    response = []

    for item in items:
        response.append(
            CartResponse(
                id=item.id,
                quantity=item.quantity,
                product={
                    "id": item.product.id,
                    "title": item.product.title,
                    "price": item.product.price,
                    "image": item.product.image,
                },
            )
        )

    return response


@router.patch("/{cart_id}", response_model=CartResponse)
def update_cart_quantity(
    cart_id: int,
    quantity: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    cart = get_cart_by_id(session, cart_id)

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found",
        )

    if cart.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden",
        )

    cart.quantity = quantity

    cart = update_cart(session, cart)

    return CartResponse(
        id=cart.id,
        quantity=cart.quantity,
        product={
            "id": cart.product.id,
            "title": cart.product.title,
            "price": cart.product.price,
            "image": cart.product.image,
        },
    )


@router.delete("/{cart_id}")
def delete_cart_item(
    cart_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    cart = get_cart_by_id(session, cart_id)

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found",
        )

    if cart.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden",
        )

    remove_cart_item(session, cart)

    return {
        "message": "Item removed"
    }


@router.delete("/")
def delete_cart(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    clear_cart(
        session,
        current_user.id,
    )

    return {
        "message": "Cart cleared"
    }