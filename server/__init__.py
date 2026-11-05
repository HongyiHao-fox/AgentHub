import os

from flask import Flask
from flask_cors import CORS

from server.blueprints.auth import bp as auth_bp
from server.blueprints.main import bp as main_bp
from server.database.db import init_app


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        MYSQL_HOST=os.getenv("MYSQL_HOST", "localhost"),
        MYSQL_PORT=int(os.getenv("MYSQL_PORT", "3306")),
        MYSQL_USER=os.getenv("MYSQL_USER", "root"),
        MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD", ""),
        MYSQL_DATABASE=os.getenv("MYSQL_DATABASE", "agent"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    init_app(app)

    return app


app = create_app()
