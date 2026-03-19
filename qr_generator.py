import os
import qrcode
from PIL import Image

url = input("Enter the URL: ").strip()
folder_name = input("Enter folder name: ").strip()

# Custom colors
custom_qr_color = input("Enter custom QR color (e.g. red, #FF5733): ").strip()
custom_bg_color = input("Enter custom background color (e.g. white, #000000)(Use Hex code from complex color): ").strip()

os.makedirs(folder_name, exist_ok=True)

qr = qrcode.QRCode(
    version=None,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# 1. Black on White
img1 = qr.make_image(fill_color="black", back_color="white")
img1.save(os.path.join(folder_name, "qr_black_on_white.png"))

# 2. Black on Transparent
img2 = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
data = img2.getdata()
new_data = []

for item in data:
    if item[:3] == (255, 255, 255):
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img2.putdata(new_data)
img2.save(os.path.join(folder_name, "qr_black_transparent.png"))

# 3. White on Transparent
img3 = qr.make_image(fill_color="white", back_color="black").convert("RGBA")
data = img3.getdata()
new_data = []

for item in data:
    if item[:3] == (0, 0, 0):
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)

img3.putdata(new_data)
img3.save(os.path.join(folder_name, "qr_white_transparent.png"))

# 4. White on Black (default requested)
img4 = qr.make_image(fill_color="white", back_color="black")
img4.save(os.path.join(folder_name, "qr_white_on_black.png"))

# 5. Custom Variant
img5 = qr.make_image(fill_color=custom_qr_color, back_color=custom_bg_color)
img5.save(os.path.join(folder_name, "qr_custom.png"))

print("All 5 QR codes generated successfully inside:", folder_name)