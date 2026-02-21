import requests
import os
import base64
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("SARVAM_API_KEY")

# Sarvam TTS endpoint
url = "https://api.sarvam.ai/text-to-speech"

# Correct authentication header
headers = {
    "api-subscription-key": API_KEY,
    "Content-Type": "application/json"
}

# Kannada text input
data = {
    "text": "ನಮಸ್ಕಾರ, ನಾನು ನಿಮ್ಮ ರಿಯಲ್ ಟೈಮ್ ಧ್ವನಿ ಸಹಾಯಕನು. ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?",
    "target_language_code": "kn-IN",
    "model": "bulbul:v3",
    "speaker": "shubh",     # Must be lowercase
    "speech_sample_rate": 24000
}

print("📤 Sending Kannada text for TTS...")

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()

    # Get base64 audio
    audio_base64 = result["audios"][0]

    # Decode base64
    audio_bytes = base64.b64decode(audio_base64)

    # Save as WAV file
    with open("output_kn.wav", "wb") as f:
        f.write(audio_bytes)

    print("✅ Kannada audio saved as output_kn.wav")
else:
    print("❌ Error:", response.status_code)
    print(response.text)