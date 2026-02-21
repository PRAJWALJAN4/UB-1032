import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")

url = "https://api.sarvam.ai/speech-to-text"  # endpoint may vary

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

files = {
    "file": ("input.wav", open("input.wav", "rb"), "audio/wav")
}

print("📤 Sending audio to Sarvam...")

response = requests.post(url, headers=headers, files=files)

print("Response status:", response.status_code)
print("Response text:", response.text)