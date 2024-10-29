from flask import Flask

from app.extension import db, cors
from app.config import Config
from app.views import bp as api_bp
from app.models import User, Patient


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cors.init_app(app)

    app.register_blueprint(api_bp)

    @app.cli.command()
    def create():
        db.drop_all()
        db.create_all()

    return app
