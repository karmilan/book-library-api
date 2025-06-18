from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import User
from app.crud import user as crud_user
from app.schemas.user import UserUpdate
from app.services.auth_service import verify_token

router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.get("/", response_model=list[User])
def get_users():
    return crud_user.get_users()


@router.get("/{id}", response_model=User)
def get_user(id):
    result = crud_user.get_user(id)
    if not result:
        raise HTTPException(status_code=404, detail="user not found")
    return result


@router.post("/")
def create_user(user: UserUpdate):
    return crud_user.create_user(user)


@router.put("/{id}")
def update_user(id, user: UserUpdate):
    return crud_user.update_user(id, user)


@router.delete("/{id}")
def delete_user(id: int):
    return crud_user.delete_user(id)
