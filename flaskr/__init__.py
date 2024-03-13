from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config
    # existing code omitted

    from . import db
    db.init_app(app)

    return app