from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


# Define the Book model to match the existing MySQL table
class User(SQLModel, table=True):
    __tablename__ = "user"  # Make sure this matches your MySQL table name
    userid: int | None = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    password: str
