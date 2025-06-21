# ui/decrypt_ui.py

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from decryptor import speech_to_text
from utils.ai_model import decode_text
from utils.file_utils import delete_file_later

def show_decrypt_ui(username):
    window = tk.Toplevel()
    window.title("Decrypt Audio")
    window.geometry("400x200")

    label = tk.Label(window, text="Select encrypted audio file")
    label.pack(pady=10)

    def choose_file():
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if not file_path:
            return

        map_path = os.path.join("assets/audio", f"{username}_map.json")
        transcribed_text = speech_to_text(file_path)

        if not transcribed_text:
            messagebox.showerror("Error", "Failed to transcribe audio.")
            return

        decrypted = decode_text(transcribed_text, map_path)
        delete_file_later(file_path, delay=30)
        delete_file_later(map_path, delay=30)

        messagebox.showinfo("Decrypted Message", decrypted)
        window.destroy()

        from ui.dashboard_ui import show_dashboard
        show_dashboard(username)

    select_btn = tk.Button(window, text="Choose Audio File", command=choose_file)
    select_btn.pack(pady=20)
