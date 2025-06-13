from pydantic import BaseModel, EmailStr


class User(BaseModel):
    userid: int
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str
    email: str


class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str
