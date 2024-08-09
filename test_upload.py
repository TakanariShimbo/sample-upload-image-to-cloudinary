import os
from dotenv import load_dotenv

import cloudinary
import cloudinary.uploader

load_dotenv()
CLOUD_NAME = os.getenv("CLOUD_NAME")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

print(f"CLOUD_NAME:{CLOUD_NAME}")
print(f"API_KEY:{API_KEY}")
print(f"API_SECRET:{API_SECRET}")

cloudinary.config(cloud_name=CLOUD_NAME, api_key=API_KEY, api_secret=API_SECRET, secure=True)

response = cloudinary.uploader.upload("https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg")

print(f"UPLOADED_IMAGE_LINK:{response['secure_url']}")
