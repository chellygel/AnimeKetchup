import requests
import os
import dotenv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

dotenv.load_dotenv(BASE_DIR / '.env')

authToken = os.environ.get('API_AUTH_TOKEN')

url = "http://127.0.0.1:8000/post/"

new_anime_data = {
    "name": "Blue Eye Samurai",
    "description": "A master of the sword lives life in disguise while "
                   "seeking revenge in Edo-period Japan.",
}

headers = {
    "Authorization": f"Token {authToken}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=new_anime_data, headers=headers)

# 201 indicates the resource was created successfully.
if response.status_code == 201:
    print("New anime listing created successfully.")
    print("Response data:", response.json())
else:
    print("Failed to create new anime listing.")
    print("Response status code:", response.status_code)
    print("Response content:", response.text)
