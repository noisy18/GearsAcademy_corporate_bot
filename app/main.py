import asyncio
from app.bot import dp, bot
from app.handlers.notify_handler import router
from app.utils.logger import setup_logger

async def main():
    setup_logger()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())