from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.config import Config

bot = Bot(token=Config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()