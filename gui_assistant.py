import tkinter as tk
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import requests
import os
import base64
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda

load_dotenv()
API_KEY = os.getenv("SARVAM_API_KEY")

# -----------------------------
# AUDIO RECORD
# -----------------------------
def record_audio(filename="input.wav", duration=5, fs=16000):
    print("Recording started...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print("Recording finished.")

# -----------------------------
# SPEECH TO TEXT
# -----------------------------
def speech_to_text():
    url = "https://api.sarvam.ai/speech-to-text"
    headers = {"api-subscription-key": API_KEY}
    files = {
        "file": ("input.wav", open("input.wav", "rb"), "audio/wav")
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        return response.json()["transcript"]
    else:
        print("STT Error:", response.text)
        return None

# -----------------------------
# LLM via LangChain
# -----------------------------
def call_llm(user_text):
    url = "https://api.sarvam.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sarvam-m",
        "messages": [
            {"role": "system", "content": "Always reply ONLY in Kannada.in 20 words"},
            {"role": "user", "content": user_text}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("LLM Error:", response.text)
        return None

# Wrap with LangChain Runnable
llm_chain = RunnableLambda(call_llm)

# -----------------------------
# TEXT TO SPEECH
# -----------------------------
def text_to_speech(text):
    url = "https://api.sarvam.ai/text-to-speech"

    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "target_language_code": "kn-IN",
        "model": "bulbul:v3",   # ✅ v3 model
        "speaker": "shubh",     # lowercase
        "speech_sample_rate": 24000,
        "temperature": 0.6      # optional but recommended
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        audio_base64 = result["audios"][0]
        audio_bytes = base64.b64decode(audio_base64)

        with open("response.wav", "wb") as f:
            f.write(audio_bytes)
    else:
        print("TTS Error:", response.text)
# -----------------------------
# PLAY AUDIO
# -----------------------------
def play_audio(filename="response.wav"):
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    sd.wait()

# -----------------------------
# MAIN ASSISTANT FUNCTION
# -----------------------------
def run_assistant():
    record_audio()
    user_text = speech_to_text()

    if not user_text:
        return

    print("User said:", user_text)

    reply = llm_chain.invoke(user_text)

    print("AI replied:", reply)

    text_to_speech(reply)
    play_audio()

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Kannada Voice Assistant")
root.geometry("300x200")

label = tk.Label(root, text="Click to Speak", font=("Arial", 14))
label.pack(pady=20)

speak_button = tk.Button(root, text="Speak", font=("Arial", 16), command=run_assistant)
speak_button.pack(pady=20)

root.mainloop()