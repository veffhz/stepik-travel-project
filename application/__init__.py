from flask import Flask

app = Flask(__name__)


def create_app():
    from . import routes, filters
    return app
