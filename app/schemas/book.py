from pydantic import BaseModel


class Book(BaseModel):
    # id: int
    title: str
    author: str
    description: str
    # status: str
    user_id: int | None = None


class BookUpdate(BaseModel):
    title: str
    author: str
    description: str
    status: str
