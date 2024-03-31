import requests

def perform_ocr(image_path, server_url):
    # Open the image file
    with open(image_path, 'rb') as file:
        # Send a POST request to the server with the image file
        files = {'image': file}
        response = requests.post(server_url, files=files)
        
        # Parse the response JSON and extract the text
        result = response.json()
        extracted_text = result['text']
        
        return extracted_text

if __name__ == '__main__':
    image_path = 'document.jpg'  # Path to the image file captured by OV5647 camera
    server_url = 'http://127.0.0.1:8080/ocr'  # URL of the OCR server
    
    extracted_text = perform_ocr(image_path, server_url)
    print("Extracted Text:")
    print(extracted_text)
