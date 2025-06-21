# main.py

import tkinter as tk
from ui.login_ui import show_login

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # hide the root window
    show_login()
    root.mainloop()
