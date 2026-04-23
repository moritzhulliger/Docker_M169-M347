from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def do_ocr():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    image = Image.open(io.BytesIO(file.read()))
    
    # Nutzt Deutsch und Englisch für bessere Erkennung
    text = pytesseract.image_to_string(image, lang='deu')
    
    return jsonify({"text": text.strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)