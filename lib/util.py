import re

from flask import abort
from itsdangerous import URLSafeSerializer

from config import ADMIN_TOKEN, TOKENAZER_SALT, TOKENAZER_SECRET_KEY
from errors.agent import BackendError


# Хотелось написать декоратор для чего то...
def validation(func):

    def wrapper(*args, **kwargs):
        print(kwargs.get("token"))
        if kwargs.get("token") != ADMIN_TOKEN:
            raise BackendError(f"Token not access!")

        return func(*args, **kwargs)

    return wrapper

# Такой же декоратор для закрепления...
def login_required(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get("auth_token"):
            abort(401)
        return func(*args, **kwargs)
    return wrapper

class RestToken:
    
    def _is_valid_email(self, email):
        if re.match(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', email):
            return True
        return False

    @property
    def _tokenazer(self):
        return URLSafeSerializer(TOKENAZER_SECRET_KEY, TOKENAZER_SALT)
        

    @classmethod
    def get(cls, email, password):
        cl = cls()

        if cl._is_valid_email(email):
            return cl._tokenazer.dumps({"email": email, "password": password})
        raise BackendError("Invalid Email adress")
    
    @classmethod
    def read(cls, token):
        if not token:
            raise BackendError("Token empty")

        cl = cls()
        return cl._tokenazer.loads(token)
