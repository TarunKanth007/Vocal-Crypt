import json

# Mapping from characters to speech-friendly tokens
CHAR_TO_TOKEN = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
    'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
    'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
    'Y': 'Yankee', 'Z': 'Zulu',
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
    ' ': 'Space', '.': 'Dot', ',': 'Comma', '?': 'hello'
}

# Reverse mapping for decryption
TOKEN_TO_CHAR = {v.upper(): k for k, v in CHAR_TO_TOKEN.items()}


def encode_text(message: str, map_path: str) -> str:
    """
    Convert input message into a sequence of speech-friendly tokens and save map.
    """
    message = message.upper()
    token_list = []

    for char in message:
        if char in CHAR_TO_TOKEN:
            token_list.append(CHAR_TO_TOKEN[char])
        else:
            token_list.append("Unknown")  # fallback for unsupported chars

    with open(map_path, 'w') as f:
        json.dump({"tokens": token_list}, f)

    return ' '.join(token_list)


def decode_text(transcribed_text: str, map_path: str) -> str:
    """
    Convert tokenized transcription back to original message using saved map.
    """
    transcribed_tokens = transcribed_text.replace(',', '').split()
    chars = []

    for token in transcribed_tokens:
        key = token.strip().upper()
        if key in TOKEN_TO_CHAR:
            chars.append(TOKEN_TO_CHAR[key])
        else:
            chars.append('?')

    return ''.join(chars)
