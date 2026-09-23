import http.server
import ssl
from pathlib import Path

HOST = "localhost"
PORT = 4443

# Folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent

CERTIFICATE_FILE = BASE_DIR / "server.crt"
PRIVATE_KEY_FILE = BASE_DIR / "server.key"

# Check that the certificate files exist
if not CERTIFICATE_FILE.exists():
    raise FileNotFoundError(f"Certificate not found: {CERTIFICATE_FILE}")

if not PRIVATE_KEY_FILE.exists():
    raise FileNotFoundError(f"Private key not found: {PRIVATE_KEY_FILE}")

# Serve files from the script's directory
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer((HOST, PORT), handler)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    certfile=str(CERTIFICATE_FILE),
    keyfile=str(PRIVATE_KEY_FILE)
)

httpd.socket = ssl_context.wrap_socket(
    httpd.socket,
    server_side=True
)

print(f"HTTPS server running at https://{HOST}:{PORT}")
print(f"Using certificate: {CERTIFICATE_FILE}")
print(f"Serving files from: {BASE_DIR}")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
finally:
    httpd.server_close()
