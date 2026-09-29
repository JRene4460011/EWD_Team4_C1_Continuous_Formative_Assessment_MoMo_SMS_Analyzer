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

    # PUT/transactions/{id}

    # DELETE/transactions/{id}



# Start the server
HOST = "localhost"
PORT = 8000

server = HTTPServer((HOST, PORT), TransactionAPI)
print(f"Server running on http://{HOST}:{PORT}")