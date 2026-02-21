import sounddevice as sd
from scipy.io.wavfile import write
import requests
import os
import base64
import soundfile as sf
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SARVAM_API_KEY")

# -------------------
# 1️⃣ Record Audio
# -------------------
def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎤 ಮಾತನಾಡಿ...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print("✅ ಧ್ವನಿ ದಾಖಲಿಸಲಾಗಿದೆ")

# -------------------
# 2️⃣ Speech to Text
# -------------------
def speech_to_text():
    url = "https://api.sarvam.ai/speech-to-text"

    headers = {
        "api-subscription-key": API_KEY
    }

    files = {
        "file": ("input.wav", open("input.wav", "rb"), "audio/wav")
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        result = response.json()
        return result["transcript"]
    else:
        print("❌ STT Error:", response.text)
        return None

# -------------------
# 3️⃣ LLM Response
# -------------------
def generate_reply(user_text):
    url = "https://api.sarvam.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
    "model": "sarvam-m",
    "messages": [
        {"role": "system", "content": "You are a helpful AI assistant. Always reply ONLY in Kannada language."},
        {"role": "user", "content": f"Reply in Kannada: {user_text}"}
    ]
}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("❌ LLM Error:", response.text)
        return None

# -------------------
# 4️⃣ Text to Speech
# -------------------
def text_to_speech(text):
    url = "https://api.sarvam.ai/text-to-speech"

    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "target_language_code": "kn-IN",
        "model": "bulbul:v3",
        "speaker": "shubh"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        audio_base64 = result["audios"][0]
        audio_bytes = base64.b64decode(audio_base64)

        with open("response.wav", "wb") as f:
            f.write(audio_bytes)

        print("🔊 ಪ್ರತಿಕ್ರಿಯೆ ಸಿದ್ಧವಾಗಿದೆ")
    else:
        print("❌ TTS Error:", response.text)

# -------------------
# 5️⃣ Play Audio
# -------------------
def play_audio(filename="response.wav"):
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    sd.wait()

# -------------------
# MAIN LOOP
# -------------------
if __name__ == "__main__":
    while True:
        record_audio()

        user_text = speech_to_text()
        if not user_text:
            continue

        print("📝 ನೀವು ಹೇಳಿದ್ದು:", user_text)

        reply = generate_reply(user_text)
        if not reply:
            continue

        print("🤖 AI:", reply)

        text_to_speech(reply)
        play_audio()

        print("--------")