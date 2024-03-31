from flask import Flask, request, jsonify
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    # Receive image file from client
    file = request.files['image']
    image = Image.open(file)
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    # Return extracted text
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Run Flask app on localhost:5000
