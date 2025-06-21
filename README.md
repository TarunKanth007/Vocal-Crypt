# StegoVoice: AI-Powered Secure Audio Messaging

StegoVoice is an AI-based voice steganography application that allows users to encrypt text messages into natural-sounding speech and later decrypt them back into the original message using ElevenLabs APIs.

This tool is designed for offline-capable secure communication. It uses randomized encryption mappings, realistic voice synthesis, and reliable speech-to-text transcription — all wrapped in a simple desktop GUI.

---

## 📸 Project Preview

https://github.com/user-attachments/assets/d9bc2f80-9ff4-4a97-8c76-b40a42d66306

_Above: Sample encryption and decryption interface_

---

## Features

- Converts secret text into human-like audio using ElevenLabs TTS
- Recovers original message via speech-to-text transcription
- Auto-deletes audio and key files after a short delay
- Access control via hardcoded authorized users
- No backend or server: all operations are local
- Tkinter-based GUI with options for encryption and decryption
- Modular file structure for easy maintenance and scaling

---

## Project Structure

- main.py : Entry point and login flow  
- credentials.py : Hardcoded user credentials  
- encryptor.py : Encrypts text using randomized AI-based mapping  
- decryptor.py : Converts audio back to text and decrypts  
- tts_converter.py : Uses ElevenLabs API to generate voice from text  
- auto_cleanup.py : Deletes temporary files after defined delay  
- ui/ : GUI logic (login, dashboard, encrypt, decrypt)  
- utils/ : Helper functions for file handling, AI mapping  
- assets/audio/ : Temporary folder for encrypted/decrypted audio  
- README.md : Project documentation  

---

## Requirements

- Python 3.10 or higher  
- ElevenLabs API key  
- Packages:
  - tkinter
  - elevenlabs
  - requests
  - json
  - os
  - threading
  - base64
  - random
  - time

Install dependencies with:

pip install elevenlabs requests

Note: tkinter is included with standard Python installations.

---

## How to Use

1. Clone or download the repository.  
2. Add your ElevenLabs API key inside the tts_converter.py and decryptor.py files.  
3. Run main.py to start the application.  
4. Log in using a predefined username and password from credentials.py.  
5. Choose to encrypt or decrypt a message.  
6. After encryption, the audio file is generated and saved temporarily.  
7. After decryption, the audio is transcribed and the original text is shown.  
8. All files are auto-deleted after 30 seconds for security.  

---

## License

This project is provided for educational and research purposes. You may adapt and expand it with credit. The ElevenLabs API used in this application is governed by its own terms of service. Do not use it for harmful or malicious purposes.

---
