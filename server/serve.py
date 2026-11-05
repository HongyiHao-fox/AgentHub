"""Backward-compatible entry module for the Flask backend."""

from server import app


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
