from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.run(port=5000)

    return app
