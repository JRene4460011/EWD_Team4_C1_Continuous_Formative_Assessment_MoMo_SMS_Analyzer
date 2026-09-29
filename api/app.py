from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
from api.auth import check_auth

# Load SMS transactions

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "dsa" / "sms_records.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    transactions = json.load(file)

# Give every transaction an ID
for index, transaction in enumerate(transactions, start=1):
    transaction["id"] = index

# API HANDLER
transaction_dictionary = {
    str(transaction["id"]): transaction
    for transaction in transactions
}
class TransactionAPI(BaseHTTPRequestHandler):

    # GET/transactions
    # GET/transactions/{id}
    def do_GET(self):

        # Check Basic Authentication
        if not check_auth(self):
            response = json.dumps({
                "error": "Authentication required"
            }).encode("utf-8")

            self.send_response(401)
            self.send_header(
                "WWW-Authenticate",
                'Basic realm="Transactions API"'
            )
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        # GET /transactions - list everything
        if self.path == "/transactions":
            response = json.dumps(transactions).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        # GET /transactions/{id} - get one by ID
        elif self.path.startswith("/transactions/"):
            try:
                transaction_id = int(self.path.split("/")[-1])
            except ValueError:
                response = json.dumps({
                    "error": "Invalid transaction ID"
                }).encode("utf-8")

                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response)))
                self.end_headers()
                self.wfile.write(response)
                return

            transaction = transaction_dictionary.get(str(transaction_id))

            if transaction is None:
                response = json.dumps({
                    "error": "Transaction not found"
                }).encode("utf-8")

                self.send_response(404)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response)))
                self.end_headers()
                self.wfile.write(response)
                return

            response = json.dumps(transaction).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        else:
            self.send_response(404)
            self.end_headers()



    # POST/transactions    
    def do_POST(self):

        if self.path == "/transactions":

            # Read the request body
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)

            # Convert JSON into a Python dictionary
            try:
                new_transaction = json.loads(post_data.decode("utf-8"))

            except json.JSONDecodeError:
                response = json.dumps({
                    "error": "Invalid JSON"
                }).encode("utf-8")

                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response)))
                self.end_headers()
                self.wfile.write(response)
                return

            # Assign a new ID to the transaction
            new_transaction["id"] = len(transactions) + 1

            # Add the transaction
            transactions.append(new_transaction)

            # Prepare the response
            response = json.dumps(new_transaction).encode("utf-8")

            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        else:
            self.send_response(404)
            self.end_headers()



    # PUT/transactions/{id}
    def do_PUT(self):
        if self.path.startswith("/transactions/"):
            transaction_id = int(self.path.split("/")[-1])
            content_length = int(self.headers.get("Content-Length", 0))
            put_data = self.rfile.read(content_length)

            try:
                updated_transaction = json.loads(put_data.decode("utf-8"))
            except json.JSONDecodeError:
                response = json.dumps({"error": "Invalid JSON"}).encode("utf-8")

                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response)))
                self.end_headers()
                self.wfile.write(response)
                return

            for transaction in transactions:
                if transaction["id"] == transaction_id:
                    transaction.update(updated_transaction)
                    transaction["id"] = transaction_id
                    response = json.dumps(transaction).encode("utf-8")

                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(response)))
                    self.end_headers()
                    self.wfile.write(response)
                    return

            # If the transaction was not found
            response = json.dumps({"error": "Transaction not found"}).encode("utf-8")

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        else:
            self.send_response(404)
            self.end_headers()

    # DELETE/transactions/{id}
    # DELETE /transactions/{id}
    def do_DELETE(self):

        # Check Basic Authentication
        if not check_auth(self):
            response = json.dumps({
                "error": "Authentication required"
            }).encode("utf-8")

            self.send_response(401)
            self.send_header(
                "WWW-Authenticate",
                'Basic realm="Transactions API"'
            )
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        # Get transaction ID
        try:
            transaction_id = int(self.path.split("/")[-1])
        except ValueError:
            response = json.dumps({
                "error": "Invalid transaction ID"
            }).encode("utf-8")

            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        # Dictionary lookup
        transaction = transaction_dictionary.get(str(transaction_id))

        if transaction is None:
            response = json.dumps({
                "error": "Transaction not found"
            }).encode("utf-8")

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        # Delete transaction
        transactions.remove(transaction)
        del transaction_dictionary[str(transaction_id)]

        response = json.dumps({
            "message": "Transaction deleted successfully",
            "transaction": transaction
        }).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


# Start the server
HOST = "localhost"
PORT = 8000

server = HTTPServer((HOST, PORT), TransactionAPI)
print(f"Server running on http://{HOST}:{PORT}")

server.serve_forever()