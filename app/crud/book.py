from fastapi import HTTPException
from sqlmodel import select
from app.models.book import Book


def get_books(session, offset, limit) -> list[Book]:
    return session.exec(select(Book).offset(offset).limit(limit)).all()


def create_books(book, session):
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
