from sqlmodel import Session, select

from app.models.category import Category


def create_category(session: Session, category: Category):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_all_categories(session: Session):
    return session.exec(select(Category)).all()

def get_category_by_id(session: Session, category_id: int):
    return session.get(Category, category_id)