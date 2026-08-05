from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.crud.product import create_product, get_all_products
from app.db.session import get_session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate

from fastapi import HTTPException
from app.crud.category import get_category_by_id
from app.crud.product import (
    create_product,
    delete_product,
    get_all_products,
    get_product_by_id,
    update_product,
)

from app.crud.product import get_product_by_slug

from typing import Optional
from fastapi import Query

from app.crud.product import search_products

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def add_product(
    product: ProductCreate,
    session: Session = Depends(get_session),
):
    if product.category_id:
        category = get_category_by_id(
            session,
            product.category_id,
    )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found",
                )
    
    db_product = Product(**product.model_dump())
    return create_product(session, db_product)

@router.get("/", response_model=list[ProductResponse])
def list_products(
    session: Session = Depends(get_session),
):
    return get_all_products(session)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    session: Session = Depends(get_session),
):
    product = get_product_by_id(session, product_id)

    if not product:
        raise HTTPException(404, "Product not found")

    return product

@router.put("/{product_id}", response_model=ProductResponse)
def edit_product(
    product_id: int,
    data: ProductUpdate,
    session: Session = Depends(get_session),
):
    product = get_product_by_id(session, product_id)

    if not product:
        raise HTTPException(404, "Product not found")

    updates = data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(product, key, value)

    return update_product(session, product)

@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    session: Session = Depends(get_session),
):
    product = get_product_by_id(session, product_id)

    if not product:
        raise HTTPException(404, "Product not found")

    delete_product(session, product)

    return {
        "message": "Product deleted successfully"
    }

@router.get("/slug/{slug}", response_model=ProductResponse)
def get_product_slug(
    slug: str,
    session: Session = Depends(get_session),
):
    product = get_product_by_slug(session, slug)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product

@router.get("/", response_model=list[ProductResponse])
def list_products(
    session: Session = Depends(get_session),
    search: Optional[str] = Query(default=None),
    category_id: Optional[int] = Query(default=None),
):
    return search_products(
        session,
        search,
        category_id,
    )