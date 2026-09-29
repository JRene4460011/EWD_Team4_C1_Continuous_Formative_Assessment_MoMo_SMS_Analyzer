from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path

# Load SMS transactions

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "dsa" / "sms_records.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    transactions = json.load(file)

# Give every transaction an ID
for index, transaction in enumerate(transactions, start=1):
    transaction["id"] = index

# API HANDLER
class TransactionAPI(BaseHTTPRequestHandler):

    # GET/transactions 

    # GET/transactions/{id}

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

        # DELETE/transactions/{id}



# Start the server
HOST = "localhost"
PORT = 8000

server = HTTPServer((HOST, PORT), TransactionAPI)
print(f"Server running on http://{HOST}:{PORT}")