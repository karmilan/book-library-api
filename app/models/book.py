from typing import Optional
from sqlmodel import Field, SQLModel


# Define the Book model to match the existing MySQL table
class Book(SQLModel, table=True):
    __tablename__ = "book"  # Make sure this matches your MySQL table name
    bookid: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    description: Optional[str] = None
    status: str = "unread"
    user_id: Optional[int] = Field(default=None)
