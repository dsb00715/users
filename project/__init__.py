from flask import Flask
from . import config


def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.DevelopmentConfig")

    return app
    