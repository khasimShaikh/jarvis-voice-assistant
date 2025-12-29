# Jarvis Voice Assistant

Jarvis is a **Python-based voice assistant** that can perform tasks like playing music, opening applications, telling jokes, providing weather updates, performing math calculations, managing files and folders, and more—all through voice commands!


## Features

- Voice recognition and response using **SpeechRecognition** and **pyttsx3**.
- Web browsing shortcuts (YouTube, Google, ChatGPT, Gmail).
- Wikipedia search and information summarization.
- Motivational quotes and riddles.
- Weather information (requires API key).
- Math calculations including percentages.
- Alarm setup with sound notification.
- Music control using **pygame** (play, pause, next, stop).
- File and folder management (create, delete, open downloads).
- Screenshot capture.
- Battery status check.
- WhatsApp message sending via **pywhatkit**.
- Sleep/wake functionality.


## Requirements

Python 3.7+ and the following libraries:

SpeechRecognition
pyttsx3
pywhatkit
pyjokes
wikipedia
pyautogui
requests
playsound
psutil
pygame
pyaudio


You can install them using:

```
pip install -r requirements.txt

```

# 1. Clone the repository:

```
git clone https://github.com/your-username/jarvis-voice-assistant.git
```
# 2. Navigate into the project folder:
```
cd jarvis-voice-assistant
```
# 3. (Optional) Create a virtual environment:
```
python -m venv venv
venv\Scripts\activate         
```
# 4. Install dependencies:
```
pip install -r requirements.txt
```
# 5. Run the assistant:
```
python main.py
```

## Notes
- APIs: Replace the placeholders in the code for quotes, riddles, and weather API with your own API keys if needed.

- Alarm sound: Replace "replace alarm sound here" with your own .mp3 file or remove the sound if you don’t want to upload audio files.

- Music directory: Update music_dir in the code to your local music folder if you want music playback.

- Contacts: Fill the contacts dictionary with phone numbers to send WhatsApp messages.

## Security
- Do not upload personal API keys or private data.

- The project is safe to share publicly if you remove .env or any sensitive files.

## License
This project is open source and free to use for learning and personal purposes.

## Author
Created by khasimShaik – a Python enthusiast and voice assistant developer.
