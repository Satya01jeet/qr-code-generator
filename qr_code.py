import qrcode as qr
from PIL import Image

img = qr.QRCode(version=1,
                error_correction=qr.constants.ERROR_CORRECT_H,
                box_size=15,
                border=1)
img.add_data('https://100xdevs.com/')
img.make(fit=True)

qrimg = img.make_image(fill_color='white', back_color='black')
qrimg.save('100xdevs.png')
