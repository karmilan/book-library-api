from fastapi import APIRouter
from app.services import auth_service as auth
from app.schemas.user import UserSignup, UserLogin

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])


@router.post("/signup/")
def signup_user(user: UserSignup):
    return auth.signup_user(user)


@router.post("/login")
def login_user(user: UserLogin):
    return auth.login_user(user)
