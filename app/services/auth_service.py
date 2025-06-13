from typing import List, Dict
from fastapi import HTTPException, Depends
from app.db.connection import get_connection
from app.schemas.user import User
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

connection = get_connection()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "1234"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# SIGNUP NEW USER
def signup_user(user):
    hashed_password = hash_password(user.password)
    sql = "INSERT INTO USER (name, email, password) VALUES (%s, %s, %s)"
    val = (user.name, user.email, hashed_password)

    cursor = connection.cursor()

    cursor.execute("SELECT userid FROM USER WHERE email = %s", (user.email,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="Email already exist")

    cursor.execute(sql, val)
    connection.commit()
    return {"msg": "user registered"}


# USER LOGIN
def login_user(user):
    cursor = connection.cursor(dictionary=True)
    print("emai:::", user.email)
    cursor.execute("SELECT * FROM USER WHERE email = %s", (user.email,))

    db_user = cursor.fetchone()
    print("db_user>>", db_user)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="invalid credentials")

    token = create_access_token({"sub": db_user["email"]})
    return {"access_token": token, "token_type": "bearer"}
