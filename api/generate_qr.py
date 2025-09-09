from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from io import BytesIO
import qrcode

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        target = q.get('url', [None])[0]
        if not target:
            self.send_response(400); self.end_headers()
            self.wfile.write(b"Missing 'url'"); return
        img = qrcode.make(target)
        buf = BytesIO(); img.save(buf, "PNG"); data = buf.getvalue()
        self.send_response(200)
        self.send_header("Content-Type","image/png")
        self.send_header("Cache-Control","public, max-age=31536000, immutable")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers(); self.wfile.write(data)

