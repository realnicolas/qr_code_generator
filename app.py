import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=40,
    border=2,
)
qr.add_data(input("The QR Code should redirect to: "))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(input("File name (All files have the extension '.png'): ") + ".png")