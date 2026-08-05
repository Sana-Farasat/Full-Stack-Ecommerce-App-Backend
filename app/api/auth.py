from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.security import create_access_token, hash_password
from app.crud.user import authenticate_user, create_user, get_user_by_email
from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse

from app.dependencies.auth import get_current_user

from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=201)
def register(
    user: UserCreate,
    session: Session = Depends(get_session),
):
    existing_user = get_user_by_email(session, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    return create_user(session, db_user)

# @router.post("/login")
# def login(
#     user: UserLogin,
#     session: Session = Depends(get_session),
# ):

#     db_user = authenticate_user(
#         session,
#         user.email,
#         user.password,
#     )

#     if not db_user:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid credentials",
#         )

#     token = create_access_token(
#         {
#             "sub": str(db_user.id)
#         }
#     )

#     return {
#         "access_token": token,
#         "token_type": "bearer",
#     }

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    db_user = authenticate_user(
        session,
        form_data.username,   # username field me email aayegi
        form_data.password,
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = create_access_token(
        {
            "sub": str(db_user.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }

@router.get("/me", response_model=UserResponse)
def me(
    current_user: User = Depends(get_current_user),
):
    return current_user