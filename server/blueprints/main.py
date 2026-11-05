from flask import Blueprint, jsonify, request

from server.services.chat import get_chat_response

bp = Blueprint("main", __name__)


@bp.route("/health")
def health():
    return jsonify({"status": "ok"})


@bp.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "")
    result = get_chat_response(message)
    return jsonify(result)
