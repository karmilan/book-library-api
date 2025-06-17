from typing import List, Dict
from app.db.connection import get_connection
from app.schemas.user import User

connection = get_connection()
cursor = connection.cursor(dictionary=True)


# GET USERS
def get_users() -> List[Dict]:
    cursor.execute("SELECT * FROM USER")
    result = cursor.fetchall()
    return result


# GET SINGLE USER
def get_user(id: int) -> Dict:
    cursor.execute("SELECT * FROM user WHERE userid = %s", (id,))
    return cursor.fetchone()


# CREATE NEW USER
def create_user(user):
    sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
    val = (user.name, user.email)
    cursor.execute(sql, val)
    connection.commit()
    return {"msg": "added"}


# UPDATE USER
def update_user(id: int, user):
    cursor.execute(
        f"UPDATE user SET name='{user.name}', email='{user.email}' WHERE userid = {id}"
    )
    connection.commit()
    return {"msg": "updated"}


# DELETE USER
def delete_user(id):
    cursor.execute("DELETE FROM user WHERE userid = %s", (id,))
    connection.commit()
    return {"msg": "deleted"}
