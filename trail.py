import requests
from PIL import Image
from io import BytesIO

# 100% public test image
url = "https://picsum.photos/200"

# Add browser-like headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code, response.headers.get("Content-Type"))

if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print("Error:", response.status_code, response.headers.get("Content-Type"))
