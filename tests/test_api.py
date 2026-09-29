import base64
import json
import threading
import unittest
from http.client import HTTPConnection
from http.server import HTTPServer

from api import app


class TransactionAPITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("localhost", 0), app.TransactionAPI)
        cls.server_thread = threading.Thread(
            target=cls.server.serve_forever,
            daemon=True,
        )
        cls.server_thread.start()
        cls.host, cls.port = cls.server.server_address

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

    def setUp(self):
        self.original_transactions = app.transactions
        self.original_dictionary = app.transaction_dictionary
        app.transactions = [
            {"id": 1, "amount": 1000, "status": "Completed"},
            {"id": 2, "amount": 2500, "status": "Pending"},
        ]
        app.transaction_dictionary = {
            str(transaction["id"]): transaction
            for transaction in app.transactions
        }

    def tearDown(self):
        app.transactions = self.original_transactions
        app.transaction_dictionary = self.original_dictionary

    def request(self, method, path, body=None, authenticated=True):
        headers = {}
        if authenticated:
            credentials = base64.b64encode(b"admin:momo2026").decode("ascii")
            headers["Authorization"] = f"Basic {credentials}"
        if body is not None:
            body = json.dumps(body)
            headers["Content-Type"] = "application/json"

        connection = HTTPConnection(self.host, self.port)
        connection.request(method, path, body=body, headers=headers)
        response = connection.getresponse()
        response_body = response.read().decode("utf-8")
        connection.close()
        data = json.loads(response_body) if response_body else None
        return response.status, data

    def test_all_endpoints_require_authentication(self):
        for method, path in (
            ("GET", "/transactions"),
            ("GET", "/transactions/1"),
            ("POST", "/transactions"),
            ("PUT", "/transactions/1"),
            ("DELETE", "/transactions/1"),
        ):
            with self.subTest(method=method, path=path):
                status, data = self.request(method, path, authenticated=False)
                self.assertEqual(status, 401)
                self.assertEqual(data["error"], "Authentication required")

    def test_get_all_transactions(self):
        status, data = self.request("GET", "/transactions")

        self.assertEqual(status, 200)
        self.assertEqual(data, app.transactions)

    def test_get_transaction_by_id(self):
        status, data = self.request("GET", "/transactions/2")

        self.assertEqual(status, 200)
        self.assertEqual(data, app.transactions[1])

    def test_get_transaction_returns_404_for_unknown_id(self):
        status, data = self.request("GET", "/transactions/99")

        self.assertEqual(status, 404)
        self.assertEqual(data["error"], "Transaction not found")

    def test_get_transaction_returns_400_for_non_numeric_id(self):
        status, data = self.request("GET", "/transactions/not-a-number")

        self.assertEqual(status, 400)
        self.assertEqual(data["error"], "Invalid transaction ID")

    def test_post_creates_transaction(self):
        transaction = {"amount": 3000, "status": "Completed"}

        status, data = self.request("POST", "/transactions", transaction)

        self.assertEqual(status, 201)
        self.assertEqual(data["id"], 3)
        self.assertEqual(data["amount"], 3000)
        self.assertIn(data, app.transactions)
        self.assertEqual(app.transaction_dictionary["3"], data)

    def test_post_returns_400_for_invalid_json(self):
        connection = HTTPConnection(self.host, self.port)
        credentials = base64.b64encode(b"admin:momo2026").decode("ascii")
        connection.request(
            "POST",
            "/transactions",
            body="{invalid",
            headers={
                "Authorization": f"Basic {credentials}",
                "Content-Type": "application/json",
            },
        )
        response = connection.getresponse()
        data = json.loads(response.read().decode("utf-8"))
        connection.close()

        self.assertEqual(response.status, 400)
        self.assertEqual(data["error"], "Invalid JSON")

    def test_put_updates_transaction(self):
        status, data = self.request(
            "PUT",
            "/transactions/1",
            {"amount": 1500, "status": "Failed"},
        )

        self.assertEqual(status, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["amount"], 1500)
        self.assertEqual(data["status"], "Failed")

    def test_put_returns_404_for_unknown_id(self):
        status, data = self.request("PUT", "/transactions/99", {"amount": 1})

        self.assertEqual(status, 404)
        self.assertEqual(data["error"], "Transaction not found")

    def test_delete_removes_transaction(self):
        status, data = self.request("DELETE", "/transactions/1")

        self.assertEqual(status, 200)
        self.assertEqual(data["message"], "Transaction deleted successfully")
        self.assertNotIn(data["transaction"], app.transactions)
        self.assertNotIn("1", app.transaction_dictionary)

    def test_delete_returns_404_for_unknown_id(self):
        status, data = self.request("DELETE", "/transactions/99")

        self.assertEqual(status, 404)
        self.assertEqual(data["error"], "Transaction not found")


if __name__ == "__main__":
    unittest.main()