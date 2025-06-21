# ui/dashboard_ui.py

import tkinter as tk
from ui.encrypt_ui import show_encrypt_ui
from ui.decrypt_ui import show_decrypt_ui

def show_dashboard(username):
    window = tk.Tk()
    window.title(f"StegoVoice Dashboard - {username}")
    window.geometry("320x220")
    window.configure(bg="#1e1e1e")

    tk.Label(window, text=f"Welcome, {username}", font=("Helvetica", 14), bg="#1e1e1e", fg="white").pack(pady=15)

    tk.Button(window, text="🔐 Encrypt Message", font=("Helvetica", 12), bg="#007acc", fg="white", width=25,
              command=lambda: [window.destroy(), show_encrypt_ui(username)]).pack(pady=10)

    tk.Button(window, text="🔓 Decrypt Message", font=("Helvetica", 12), bg="#007acc", fg="white", width=25,
              command=lambda: [window.destroy(), show_decrypt_ui(username)]).pack(pady=10)

    window.mainloop()
