from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L

def generate_qr(text):
  qr = QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=2,
  )
  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color='#000', back_color='#fff')
  return img