from flask import Flask


def create_app():
    application = Flask(__name__)
    application.config.from_pyfile('settings.py')
    return application


app = create_app()

from webapp import views
