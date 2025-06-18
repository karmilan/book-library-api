from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import books, users, auth

# from app.api.v1.routes import auth

app = FastAPI()

# Allow frontend from this origin (adjust in production)
origins = [
    "http://localhost:3000",  # Next.js dev server
    "http://127.0.0.1:3000",
    "https://bookly-two-phi.vercel.app/",  # Vercel deployment URL
]

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow specific domains
    allow_credentials=True,  # if sending cookies (optional)
    allow_methods=["*"],  # allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # allow all headers (Authorization, etc.)
)

# include user route
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Bookstore API!"}
