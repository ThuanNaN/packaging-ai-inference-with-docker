import os
import requests
import io
from PIL import Image
from utils import plot_bbox

BACKEND_URL = os.getenv("BACKEND_URL", "http://0.0.0.0:8000")

def ocr_api(image_path: str):
    if image_path is None:
        return "Please upload an image first.", None

    image = Image.open(image_path).convert("RGB")
    img_name = os.path.basename(image_path)
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    url = f"{BACKEND_URL}/ocr/predict"
    files = {'file_upload': (img_name, img_byte_arr, 'image/jpeg')}
    headers = {'accept': 'application/json'}

    try:
        response = requests.post(url, headers=headers, files=files, timeout=60)
    except requests.RequestException as e:
        return f"Error: cannot reach backend ({e.__class__.__name__}).", None

    if response.status_code == 200:
        json_results = response.json()['data']
        image_with_bbox = plot_bbox(json_results, image)[0]
        return f"Success: {len(json_results)} text line(s) found.", image_with_bbox
    else:
        return f"Error: API request failed ({response.status_code}).", None
