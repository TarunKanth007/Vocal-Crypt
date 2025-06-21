import os
import threading
import time

def delete_file_later(file_path, delay=30):
    def delete():
        time.sleep(delay)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"[🗑️] Auto-deleted {file_path}")
            except Exception as e:
                print(f"[✗] Error deleting file {file_path}: {e}")
    threading.Thread(target=delete).start()
