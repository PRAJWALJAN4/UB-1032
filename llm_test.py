import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")

url = "https://api.sarvam.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "sarvam-m",   # default Sarvam chat model
    "messages": [
        {"role": "system", "content": "You are a helpful voice assistant."},
        {"role": "user", "content": "Hello"}
    ]
}

print("📤 Sending text to Sarvam LLM...")

response = requests.post(url, headers=headers, json=data)

print("Status:", response.status_code)
print("Response:", response.text)