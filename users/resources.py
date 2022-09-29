from flask_restful import Resource, reqparse
from .services import UsersService


class Base():
    __service__ = UsersService

    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help='Informe um email'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='Informe uma senha'
    )


class UserCreation(Resource, Base):
    def post(self):
        data = UserCreation.parser.parse_args()
        return self.__service__.create(**data)


class UserLogin(Resource, Base):
    def post(self):
        data = UserCreation.parser.parse_args()
        return self.__service__.login(**data)
