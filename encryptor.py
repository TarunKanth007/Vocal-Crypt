# encryptor.py

from utils.ai_model import encode_text

def ai_encrypt(plain_text: str) -> str:
    print(f"[🔐] Original: {plain_text}")
    encrypted = encode_text(plain_text)
    print(f"[🔒] Encrypted (AI scramble): {encrypted}")
    return encrypted
