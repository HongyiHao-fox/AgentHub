import functools

from flask import Blueprint, current_app, flash, g, jsonify, redirect, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from server.database.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/status")
def auth_status():
    return jsonify({"auth": "ready"})


@bp.route("/register", methods=("POST",))
def register():
    if not current_app.config.get("MYSQL_READY", True):
        return jsonify({"error": "MySQL is not ready. Please configure MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD and MYSQL_DATABASE."}), 503

    payload = request.get_json(silent=True) or {}
    username = payload.get("username", "")
    password = payload.get("password", "")
    error = None

    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."

    if error is None:
        db = get_db()
        try:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            error = f"User {username} is already registered."

    if error is not None:
        return jsonify({"error": error}), 400

    return jsonify({"message": f"User {username} registered"})


@bp.route("/login", methods=("POST",))
def login():
    if not current_app.config.get("MYSQL_READY", True):
        return jsonify({"error": "MySQL is not ready. Please configure MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD and MYSQL_DATABASE."}), 503

    payload = request.get_json(silent=True) or {}
    username = payload.get("username", "")
    password = payload.get("password", "")
    db = get_db()
    error = None
    user = db.execute(
        "SELECT * FROM user WHERE username = ?", (username,)
    ).fetchone()

    if user is None:
        error = "Incorrect username."
    elif not check_password_hash(user["password"], password):
        error = "Incorrect password."

    if error is not None:
        return jsonify({"error": error}), 400

    session.clear()
    session["user_id"] = user["id"]
    return jsonify({"message": f"User {username} logged in"})


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()


@bp.route("/logout")
def logout():
    session.clear()
    return jsonify({"message": "logged out"})


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return jsonify({"error": "login required"}), 401
        return view(**kwargs)

    return wrapped_view