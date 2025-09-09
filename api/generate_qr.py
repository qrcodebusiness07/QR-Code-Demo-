from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from io import BytesIO
import qrcode

DEFAULT_TARGET = "https://qrcodebusiness07.github.io/QR-Code-Demo-/"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        target = q.get('url', [None])[0] or DEFAULT_TARGET

        img = qrcode.make(target)
        buf = BytesIO(); img.save(buf, "PNG"); data = buf.getvalue()

        self.send_response(200)
        self.send_header("Content-Type","image/png")
        self.send_header("Cache-Control","public, max-age=31536000, immutable")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers(); self.wfile.write(data)
