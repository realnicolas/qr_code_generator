import qrcode
import uuid

qr = qrcode.QRCode(
    version=1,
    box_size=40,
    border=2,
)
qr.add_data(input("The QR Code should redirect to: "))
filename = input("File name (All files will be saved with the extension '.png'): ")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"./codes/{filename}{uuid.uuid4()}.png")