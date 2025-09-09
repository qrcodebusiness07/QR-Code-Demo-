import qrcode
from pathlib import Path

TARGET_URL = "https://qrcodebusiness07.github.io/QR-Code-Demo-/"

out_path = Path(__file__).parent / "restaurant-menu-qr.png"
img = qrcode.make(TARGET_URL)
img.save(out_path)
print(f"Saved QR code to {out_path.resolve()}")
