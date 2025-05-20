from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start, add_task
from config import Config
from database import db
import asyncio
from handlers import help_command




def main():
    application = ApplicationBuilder().token(Config.TELEGRAM_TOKEN).build()
    
    # \u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u043e\u0432
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_task))
    # \u0414\u0440\u0443\u0433\u0438\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0438...
    application.add_handler(CommandHandler("help", help_command))
    # \u0417\u0430\u043f\u0443\u0441\u043a \u0431\u043e\u0442\u0430
    application.run_polling()

if __name__ == '__main__':
    main()