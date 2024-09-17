#Thanks to Realpython.com

import segno

qrcode = segno.make_qr("https://youtube.com/@JohnDoeSec")
qrcode.save("basic_qrcode.png", scale=10, light=(0,255,0))
