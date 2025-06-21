# tts_converter.py

from elevenlabs.client import ElevenLabs
import os
import time

# Set your API key
client = ElevenLabs(api_key="Your-key")

def text_to_speech(text, output_path):
    try:
        response = client.text_to_speech.convert(
            voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel voice
            model_id="eleven_multilingual_v2",
            text=text,
            output_format="mp3_44100_128"
        )
        # Write audio
        with open(output_path, "wb") as f:
            for chunk in response:
                f.write(chunk)
            f.flush()
        time.sleep(0.5)  # ensure file is saved
        print(f"[✓] Audio saved at {output_path}")
    except Exception as e:
        print(f"[✗] Text-to-speech failed: {e}")
