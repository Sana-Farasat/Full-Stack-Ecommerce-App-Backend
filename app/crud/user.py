from sqlmodel import Session, select

from app.models.user import User
from app.core.security import verify_password


def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def authenticate_user(session, email, password):

    user = get_user_by_email(session, email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user