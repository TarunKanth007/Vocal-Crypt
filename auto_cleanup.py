# auto_cleanup.py

import os
import threading
import time

def delete_file_after_delay(file_path, delay_seconds=30):
    def delete():
        try:
            time.sleep(delay_seconds)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"[🗑️] Auto-deleted {file_path}")
            else:
                print(f"[⚠️] File already deleted or not found: {file_path}")
        except Exception as e:
            print(f"[✗] Auto-deletion failed: {e}")

    threading.Thread(target=delete, daemon=True).start()
