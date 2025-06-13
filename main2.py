from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI(
    title="library management", description="crud api for library", version="0.1.1"
)

db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="book_library"
)

cursor = db.cursor()


class User(BaseModel):
    # userid: int
    name: str
    email: str


# GET USERS
@app.get("/user")
def get_user():
    cursor.execute("SELECT * FROM USER")
    result = cursor.fetchall()
    return {"users": result}


# GET SINGLE USER
@app.get("/user/{id}")
def get_single_user(id: int):
    cursor.execute(f"SELECT * FROM USER WHERE userid = {id}")
    result = cursor.fetchone()
    return {"user": result}


# POST USER
@app.post("/user")
def create_user(user: User):
    cursor.execute(
        f"INSERT INTO USER (name, email) VALUES ('{user.name}','{user.email}')"
    )
    db.commit()
    return {"msg": "user added"}


# PUT USER
@app.put("/user/{id}")
def update_user(id: int, user: User):
    cursor.execute(
        f"UPDATE USER SET name='{user.name}', email='{user.email}' WHERE userid = {id}"
    )
    db.commit()
    return {"msg": "updated"}


# DELETE USER
@app.delete("/user/{id}")
def delete_user(id: int):
    cursor.execute(f"SELECT * FROM USER WHERE userid={id}")
    result = cursor.fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="user not found")
    cursor.execute(f"DELETE FROM USER WHERE userid={id}")
    cursor.execute()
    db.commit()
    return {"msg": "user deleted"}
