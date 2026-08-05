from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.crud.category import create_category, get_all_categories
from app.db.session import get_session
from app.models.category import Category
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("/", response_model=CategoryResponse)
def add_category(
    category: CategoryCreate,
    session: Session = Depends(get_session),
):
    db_category = Category(**category.model_dump())
    return create_category(session, db_category)


@router.get("/", response_model=list[CategoryResponse])
def list_categories(
    session: Session = Depends(get_session),
):
    return get_all_categories(session)