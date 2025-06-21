# ui/login_ui.py

import tkinter as tk
from tkinter import messagebox
from credentials import authorized_users
from ui.dashboard_ui import show_dashboard

def show_login():
    global window, username_entry, password_entry

    window = tk.Tk()
    window.title("StegoVoice Login")
    window.geometry("300x200")
    window.configure(bg="#1e1e1e")

    tk.Label(window, text="Username", fg="white", bg="#1e1e1e").pack(pady=5)
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="Password", fg="white", bg="#1e1e1e").pack(pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    tk.Button(window, text="Login", bg="#007acc", fg="white", width=15, command=try_login).pack(pady=15)

    window.mainloop()

def try_login():
    username = username_entry.get()
    password = password_entry.get()

    if username in authorized_users and authorized_users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        window.destroy()
        show_dashboard(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
