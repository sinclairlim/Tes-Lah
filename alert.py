import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# 🚀 Explicitly load .env file from same directory
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("🧪 DEBUG: Loaded from .env:")
print("TELEGRAM_BOT_TOKEN:", BOT_TOKEN)
print("TELEGRAM_CHAT_ID:", CHAT_ID)

def send_notification(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("⚠️ Telegram credentials missing in .env")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("📲 Notification sent!")
        else:
            print(f"⚠️ Failed to send alert: {response.text}")
    except Exception as e:
        print(f"❌ Error sending notification: {e}")
