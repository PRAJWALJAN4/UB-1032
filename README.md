# UB-1032

🌾 Krushi-Mitra
Kannada AI Voice Assistant using Sarvam API + LangChain + GUI

Krushi-Mitra is a real-time Kannada AI voice assistant built using:

🎤 Speech-to-Text (Sarvam STT)

🧠 Sarvam LLM (Chat Completions)

🔊 Sarvam Text-to-Speech (bulbul:v3)

🖥 Tkinter Animated GUI

🔗 LangChain (Runnable integration)

🐍 Python 3.13

🚀 Features

🎨 Modern animated circular GUI

🌊 Dynamic wave animation

🎙 Microphone voice input

🧠 AI-generated Kannada responses

🔊 Natural Kannada voice output (bulbul:v3)

🧵 Threaded execution (non-blocking UI)

🔐 API key secured via .env

🧩 Modular file structure

📁 Project Structure
sarvam_voice_assistant/
│
├── assistant.py           # Terminal-based voice assistant
├── gui_assistant.py       # Full animated GUI assistant (main app)
├── mic_test.py            # Microphone recording test
├── stt_test.py            # Speech-to-text test
├── llm_test.py            # LLM response test
├── tts_test.py            # Text-to-speech test
│
├── input.wav              # Recorded user audio
├── response.wav           # AI response audio
├── output.wav             # TTS output file
├── output_kn.wav          # Kannada TTS output
│
├── .env                   # Stores Sarvam API key (not committed)
├── venv/                  # Virtual environment
└── README.md              # Project documentation
🛠 Installation
1️⃣ Clone the repository
git clone https://github.com/PRAJWALJAN4/UB-1032/
cd krushi-mitra
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install sounddevice scipy soundfile requests python-dotenv langchain langchain-core langchain-community
4️⃣ Add your Sarvam API key

Create a file:

.env

Inside it:

SARVAM_API_KEY=your_api_key_here

⚠ Do NOT commit .env to GitHub.

▶ Run the GUI Assistant
python gui_assistant.py

Click 🎤 and speak.

The assistant will:

Record your voice

Convert speech to text

Generate Kannada AI response

Convert text to speech

Play the response

🧠 Technologies Used
Component	Technology
GUI	Tkinter
Animation	Canvas + Math Wave
STT	Sarvam Speech-to-Text
LLM	Sarvam Chat API
TTS	Sarvam bulbul:v3
Orchestration	LangChain Runnable
Audio	sounddevice + soundfile
🎧 Supported Language

Kannada (kn-IN)

English input supported (auto-translated by LLM)

🔮 Future Improvements

🌊 Real-time audio amplitude-based waveform

🌙 Dark mode UI

🎙 Continuous listening mode

💬 Conversation memory

📊 Live speech visualization

☁ Cloud deployment

📱 Android version

🧠 Context-aware agriculture advisory mode

🌱 Vision

Krushi-Mitra aims to become:

A conversational AI assistant for farmers,
providing voice-based agricultural guidance in Kannada.

👨‍💻 Authors

Team Cronix
B.Tech Computer Science
Project: Krushi-Mitra
