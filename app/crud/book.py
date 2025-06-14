from fastapi import HTTPException
from sqlmodel import select
from app.crud.user import get_user
from app.models.book import Book


def get_books(session, offset, limit) -> list[Book]:
    return session.exec(select(Book).offset(offset).limit(limit)).all()


def get_books_by_user(user_id, session, offset, limit) -> list[Book]:
    books = session.exec(
        select(Book).where(Book.user_id == user_id).offset(offset).limit(limit)
    ).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found for this user")
    return books


def create_books(book, session):
    user = get_user(book.user_id)  # Ensure user exists
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def update_book(bookid, book_update, session):
    book = session.get(Book, bookid)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")

    update_data = book_update.model_dump()
    for key, value in update_data.items():
        setattr(book, key, value)

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def delete_book(bookid, session):
    book = session.get(Book, bookid)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    session.delete(book)
    session.commit()
    return {"msg": "deleted"}
