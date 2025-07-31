import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    TELEGRAM_GROUP_ID = int(os.getenv("TELEGRAM_GROUP_ID"))
    TOPIC_ID = int(os.getenv("TOPIC_ID"))
    