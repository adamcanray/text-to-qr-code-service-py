from flask import Flask, send_file, request
from io import BytesIO
from generator import generate_qr

app = Flask(__name__)

@app.route('/qrimg', methods=['GET'])
def qrimg():
  text = request.args.get('text')
  if text is None or not text:
    return 'nothing to show.'
  img_buf = BytesIO()
  img = generate_qr(text)
  img.save(img_buf)
  img_buf.seek(0) 
  return send_file(
    img_buf,
    mimetype='png',
    # as_attachment=True,
    # download_name='qr-code.png',
  )

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)