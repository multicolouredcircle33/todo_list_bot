from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm your To-Do List Bot.\n\n"
        "I can help you add tasks, remind you when it's time, "
        "and manage your daily activities.\n\n"
        "Type /help to see what I can do."
    )
