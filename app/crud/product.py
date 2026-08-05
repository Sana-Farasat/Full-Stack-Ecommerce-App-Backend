from sqlmodel import Session, select

from app.models.product import Product

def create_product(session: Session, product: Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def get_all_products(session: Session):
    return session.exec(select(Product)).all()


def get_product_by_slug(session: Session, slug: str):
    statement = select(Product).where(Product.slug == slug)
    return session.exec(statement).first()

def get_product_by_id(session: Session, product_id: int):
    return session.get(Product, product_id)


def update_product(session: Session, product: Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def delete_product(session: Session, product: Product):
    session.delete(product)
    session.commit()

def get_product_by_slug(session: Session, slug: str):
    statement = select(Product).where(Product.slug == slug)
    return session.exec(statement).first()

def search_products(
    session: Session,
    search: str | None = None,
    category_id: int | None = None,
):
    statement = select(Product)

    if search:
        statement = statement.where(
            Product.title.contains(search)
        )

    if category_id:
        statement = statement.where(
            Product.category_id == category_id
        )

    return session.exec(statement).all()