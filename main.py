from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import help_command, start, add_task
from config import Config
import logging
from database import db
import asyncio

# Настройка логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    try:
        app = ApplicationBuilder().token(Config.TELEGRAM_TOKEN).build()
        
        # Регистрируем команды
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("add", add_task))
        
        print("Бот успешно запущен!")
        app.run_polling()
        
    except Exception as e:
        logging.error(f"Ошибка запуска бота: {e}")

if __name__ == "__main__":
    main()