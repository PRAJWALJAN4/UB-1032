import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # Sample rate
seconds = 5  # Duration of recording

print("🎤 Speak now...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()

write("input.wav", fs, recording)

print("✅ Recording saved as input.wav")