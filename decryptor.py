# decryptor.py

import os
from elevenlabs.client import ElevenLabs
from utils.ai_model import decode_text

client = ElevenLabs(api_key="Your-key")

def speech_to_text(audio_path):
    # Validate file existence
    if not os.path.exists(audio_path) or os.path.getsize(audio_path) < 1000:
        print(f"[✗] File missing or corrupted: {audio_path}")
        return ""

    try:
        with open(audio_path, "rb") as audio_file:
            response = client.speech_to_text.convert(
                file=audio_file,
                model_id="scribe_v1"
            )

        # ✅ FIXED: access `.text` attribute directly
        transcribed_text = response.text
        print(f"[🧾] Transcribed: {transcribed_text}")
        return transcribed_text.strip().lower()

    except Exception as e:
        print(f"[✗] Speech-to-text failed: {e}")
        return ""

def ai_decrypt(transcribed_text: str) -> str:
    print(f"[🔍] Raw transcription: {transcribed_text}")
    decrypted = decode_text(transcribed_text)
    print(f"[✅] Decrypted: {decrypted}")
    return decrypted
