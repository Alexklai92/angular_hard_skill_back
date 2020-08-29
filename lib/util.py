from errors.agent import BackendError
from config import ADMIN_TOKEN

# Хотелось написать декоратор для чего то...
def validation(func):

    def wrapper(*args, **kwargs):
        if kwargs.get("token") != ADMIN_TOKEN:
            raise BackendError(f"Token not access!")

        func(*args, **kwargs)

    return wrapper

# Такой же декоратор для закрепления...
def login_required(func):
    
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    
    return wrapper
