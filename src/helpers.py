from src.app import db
from src.models.User import User
from bcrypt import hashpw, gensalt, checkpw 
from base64 import b64encode 
from hashlib import sha256 


def get_users():
    """
    Function intended to query database for all users
    """

    users = User.get_all()
    # return [{"id": i.id, "username": i.username, "pwd": i.pwd} for i in users]
    return [i for i in users]


def get_user(uid):
    """
    Function intended to query database for user by id
    """

    users = User.query.all()
    user = list(filter(lambda x: x.id == uid, users))[0]
    return {"firstName": user.firstName, "lastName": user.lastName, "email": user.email, "address": user.address}
    # return {"id": user.id, "username": user.username, "pwd": user.pwd}


def add_user(username, pwd):
    """
    Function intended to add users, pass variables with values not values themselves
    """

    if username and pwd :
        try:
            user = User(username, pwd)
            user.save()
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False


def remove_user(user_id):
    """
    Function intended to remove users
    """

    if user_id:
        try:
            user = User.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False


def encrypt_pwd(pwd):
    """
    Hash pwd provided
    """
    return hashpw(b64encode(sha256(pwd.encode()).digest()), gensalt()).decode()


def check_pwd(x, y):
    """ 
    Check whether password hashed matches:
        * arg x** password to check
        * arg y** original hashed password
    """
    return checkpw(b64encode(sha256(x.encode()).digest()), y.encode())