from werkzeug.exceptions import HTTPException


class QuantityException(HTTPException):
    code = 400
