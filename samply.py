import os 
import json 
import requests 
from load_dotenv import load_dotenv

load_dotenv()

# URL = "https://api.imgflip.com/get_memes"
# response = requests.get(URL).json()
# print(response)
# print(f"\nNumber of Memes: {len(response['data']['memes'])}")

# [Robin]: "I work best under pressure."  
# [Batman]: "Then prepare for an explosion."


# /caption_image 
URL = "https://api.imgflip.com/caption_image"
payload = {
        "template_id": 438680,
        "username": os.environ.get("IMG_FLIP_USERNAME"),
        "password": os.environ.get("IMG_FLIP_PASSWORD"),
        "text0": "I work best under pressure.",
        "text1": "Then prepare for an explosion."
    }
response = requests.post(URL, data=payload)
result = response.json()
print(result)