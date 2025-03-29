import os
import time
from uploader import upload_event_folder
from alert import send_notification

WATCH_PATH = './mock_SentryClips'
SEEN = set()

def scan():
    current = set(os.listdir(WATCH_PATH))
    new = current - SEEN

    for folder in new:
        full_path = os.path.join(WATCH_PATH, folder)
        if os.path.isdir(full_path):
            print(f"🚨 Detected new Sentry event: {folder}")
            upload_event_folder(full_path)
            send_notification(f"📤 New Tesla Sentry event: {folder}")

    return current

if __name__ == "__main__":
    print("👀 Scanning for Sentry events...")
    os.makedirs(WATCH_PATH, exist_ok=True)

    while True:
        SEEN = scan()
        time.sleep(2)
