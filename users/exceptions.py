from curses.ascii import HT
from werkzeug.exceptions import HTTPException


class UserAlreadyExistsException(HTTPException):
    code = 400


class UserEmailOrPasswordInvalidException(HTTPException):
    code = 404
