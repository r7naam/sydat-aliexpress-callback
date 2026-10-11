from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path)

        if path.path == "/callback":
            print("Callback request received (details hidden).", flush=True)
            message = "AliExpress callback received."
        elif path.path == "/":
            message = "SydatAliExpress callback service is running."
        else:
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode())

port = int(os.environ.get("PORT", "10000"))
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
