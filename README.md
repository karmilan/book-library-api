# Book Library API

A FastAPI-based RESTful API for managing a book library.

## Features

- Add, update, delete, and retrieve books
- Search books by title, author, or genre
- Pagination and filtering support

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

```bash
git clone https://github.com/yourusername/book-library-api.git
cd book-library-api
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## API Documentation

Interactive docs available at:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## License

MIT License
