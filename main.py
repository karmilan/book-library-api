from fastapi import FastAPI

from app.api.v1.routes import books, users, auth

# from app.api.v1.routes import auth

app = FastAPI()

# include user route
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(books.router)
