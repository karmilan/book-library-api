from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.crud import book as crud_book
from app.db.session import get_session
from app.models.book import Book
from app.schemas.book import BookUpdate

router = APIRouter(prefix="/api/v1/books", tags=["books"])

SessionDep = Annotated[Session, Depends(get_session)]


@router.get("/")
def get_books(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    print("book route")
    return crud_book.get_books(session, offset, limit)


@router.post("/")
def create_books(book: Book, session: SessionDep):
    return crud_book.create_books(book, session)


@router.put("/{bookid}")
def update_book(bookid: int, book_update: BookUpdate, session: SessionDep):
    return crud_book.update_book(bookid, book_update, session)


@router.delete("/{bookid}")
def delete_book(bookid: int, session: SessionDep):
    return crud_book.delete_book(bookid, session)
