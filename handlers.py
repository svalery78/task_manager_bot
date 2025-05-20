from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
from database import db, Task
from ai_helper import generate_ai_response
import datetime
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я твой AI-помощник с виртуальным питомцем. "
        "Давай начнем управлять твоими задачами!"
    )



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 *Помощь по командам бота-ассистента* 🤖

*Основные команды:*
/start - Начать работу с ботом
/help - Показать это сообщение
/add - Добавить новую задачу (можно просто написать текст задачи)
/list - Показать все ваши задачи
/edit - Изменить существующую задачу
/done [ID] - Отметить задачу как выполненную
/delete [ID] - Удалить задачу

*Особенности бота:*
🐾 _Виртуальный питомец_ - растет вместе с вашими достижениями
⏰ _Автонапоминания_ - бот напомнит о задачах в указанное время
📊 _Аналитика_ - еженедельные отчеты о вашей продуктивности
💡 _AI-советы_ - персональные рекомендации по тайм-менеджменту

*Примеры использования:*
1. Просто напишите "Купить молоко завтра в 18:00" - бот сам распознает задачу и время
2. Ответьте "Изменить на 19:00" на напоминание, чтобы перенести время
3. Напишите "Добавить к задаче 5: купить еще хлеб" для уточнения

*Ваш виртуальный питомец:*
🐣 Уровень 1: 0-10 выполненных задач
🐥 Уровень 2: 11-30 задач
🐔 Уровень 3: 31+ задач

Для связи с разработчиком: @your_username
"""

    await update.message.reply_text(help_text, parse_mode='Markdown')

#async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Реализация добавления задачи
#    pass
async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    task_text = update.message.text
    
    # Сохраняем задачу в БД
    task_id = db.add_task(user_id, task_text)
    
    # AI-ответ через OpenRouter
    ai_response = await generate_ai_response(
        f"Пользователь добавил задачу: {task_text}. Подтверди добавление и предложи следующий шаг."
    )
    
    await update.message.reply_text(ai_response)
# Другие обработчики...