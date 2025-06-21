# ui/encrypt_ui.py

import os
import tkinter as tk
from tkinter import messagebox
from tts_converter import text_to_speech
from utils.ai_model import encode_text
from utils.file_utils import delete_file_later

def show_encrypt_ui(username):
    window = tk.Toplevel()
    window.title("Encrypt Message")
    window.geometry("400x300")

    label = tk.Label(window, text="Enter your message:")
    label.pack(pady=10)

    text_entry = tk.Text(window, height=5, width=40)
    text_entry.pack(pady=10)

    def encrypt():
        user_input = text_entry.get("1.0", tk.END).strip()
        if not user_input:
            messagebox.showerror("Error", "Please enter a message.")
            return

        filename = f"{username}_encrypted.mp3"
        audio_path = os.path.join("assets/audio", filename)
        map_path = os.path.join("assets/audio", f"{username}_map.json")

        try:
            encrypted = encode_text(user_input, map_path)
            text_to_speech(encrypted, audio_path)

            delete_file_later(audio_path, delay=30)
            delete_file_later(map_path, delay=30)

            messagebox.showinfo("Success", f"Audio saved as {filename} and will auto-delete in 30s.")
            window.destroy()

            from ui.dashboard_ui import show_dashboard
            show_dashboard(username)

        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    encrypt_btn = tk.Button(window, text="Encrypt & Generate Audio", command=encrypt)
    encrypt_btn.pack(pady=20)
