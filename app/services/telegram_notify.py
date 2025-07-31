from datetime import datetime

from app.bot import bot
from app.config import Config


async def send_application_to_topic(data: dict):

    dt = datetime.fromisoformat(data['created_at'])
    formatted_date = dt.strftime('%d.%m.%Y')
    formatted_time = dt.strftime('%H:%M')

    message = (
        f"<b>Новая заявка на пробный урок</b>\n"
        f"\n"
        f"<b>🕒 Время создания заявки</b>\n"
        f"Дата: {formatted_date}\n"
        f"Время: {formatted_time}\n"
        f"\n"
        f"📍 Имя: {data['name']}\n"
        f"📍 Фамилия: {data['surname']}\n"
        f"📧 Почта: {data['email']}\n"
        f"📞 Телефон: {data['phone']}"
    )

    await bot.send_message(
        chat_id=Config.TELEGRAM_GROUP_ID,
        text=message,
        message_thread_id=Config.TOPIC_ID
    )