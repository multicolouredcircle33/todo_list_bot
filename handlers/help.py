from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🆘 *To-Do Bot Help*\n\n"
        "/add – Add a new task\n"
        "/list – View your tasks\n"
        "/complete – Mark a task as completed\n"
        "/delete – Delete a task\n"
        "/help – Show this help message",
        parse_mode="Markdown")