from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
from database import db, Task
from ai_helper import generate_ai_response
import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я твой AI-помощник с виртуальным питомцем. "
        "Давай начнем управлять твоими задачами!"
    )

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        task_text = update.message.text.replace('/add', '').strip()
        
        if not task_text:
            await update.message.reply_text("Пожалуйста, укажите текст задачи после команды /add")
            return
        
        # Добавляем задачу в БД
        task_id = db.add_task(user_id, task_text)
        
        await update.message.reply_text(
            f"✅ Задача #{task_id} добавлена!\n"
            f"Текст: {task_text}"
        )
    except Exception as e:
        print(f"Ошибка при добавлении задачи: {e}")
        await update.message.reply_text("⚠️ Не удалось добавить задачу")

# Другие обработчики...

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        help_text = "Справка по боту:\n\n" \
                   "/start - Начать работу\n" \
                   "/add - Добавить задачу\n" \
                   "/list - Список задач\n" \
                   "/edit - Изменить задачу\n" \
                   "/done - Отметить как выполненную\n" \
                   "/delete - Удалить задачу\n" \
                   "/help - Эта справка"
        
        await update.message.reply_text(help_text)
    except Exception as e:
        print(f"Ошибка в help_command: {str(e)}")
        await update.message.reply_text("⚠️ Не удалось отобразить справку")