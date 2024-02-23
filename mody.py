from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "29035333")
APP_HASH = os.environ.get("APP_HASH", "85d2357d1e0e5b3399aaa3c7bf01dd4f")
SESSION = os.environ.get("SESSION")
elhzeyba = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
elhzeyba.start()
