
import qrcode

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data('''开票资料
test
''')
qr.make()

img = qr.make_image()

img.save("E:\\bill.png")