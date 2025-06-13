from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str


class BookUpdate(BaseModel):
    title: str
    author: str
    description: str
