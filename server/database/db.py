from contextlib import closing

import pymysql
from flask import current_app, g


def get_db():
    if "db" not in g:
        conn = pymysql.connect(
            host=current_app.config.get("MYSQL_HOST", "localhost"),
            port=current_app.config.get("MYSQL_PORT", 3306),
            user=current_app.config.get("MYSQL_USER", "root"),
            password=current_app.config.get("MYSQL_PASSWORD", ""),
            database=current_app.config.get("MYSQL_DATABASE", "agent"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        g.db = conn
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with closing(db.cursor()) as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS post (
                id INT AUTO_INCREMENT PRIMARY KEY,
                author_id INT NOT NULL,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                title VARCHAR(255) NOT NULL,
                body TEXT NOT NULL,
                FOREIGN KEY (author_id) REFERENCES user(id)
            )
            """
        )
    db.commit()


def init_app(app):
    app.teardown_appcontext(close_db)

    with app.app_context():
        try:
            init_db()
        except pymysql.MySQLError as exc:
            app.logger.warning("MySQL initialization failed: %s", exc)
            app.config["MYSQL_READY"] = False
        else:
            app.config["MYSQL_READY"] = True