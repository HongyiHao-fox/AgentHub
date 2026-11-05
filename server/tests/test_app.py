import os
import unittest

from server import create_app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "MYSQL_HOST": os.getenv("MYSQL_HOST", "localhost"),
            "MYSQL_PORT": int(os.getenv("MYSQL_PORT", "3306")),
            "MYSQL_USER": os.getenv("MYSQL_USER", "root"),
            "MYSQL_PASSWORD": os.getenv("MYSQL_PASSWORD", ""),
            "MYSQL_DATABASE": os.getenv("MYSQL_DATABASE", "agent"),
        })
        self.client = self.app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_auth_status(self):
        response = self.client.get("/auth/status")
        self.assertEqual(response.status_code, 200)
        self.assertIn("auth", response.get_json())

    def test_chat(self):
        response = self.client.post(
            "/chat",
            json={"message": "你好"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.get_json())

    def test_register_and_login(self):
        register_response = self.client.post(
            "/auth/register",
            json={"username": "alice", "password": "secret"},
        )
        self.assertEqual(register_response.status_code, 200)

        login_response = self.client.post(
            "/auth/login",
            json={"username": "alice", "password": "secret"},
        )
        self.assertEqual(login_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
