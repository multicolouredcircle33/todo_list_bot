from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("*To-Do Bot Help:*\n\n"
        "Simply use the following commands to manage your tasks:\n\n"
        "/start – Start the bot and see the welcome message\n"                            
        "/add – Add a new task\n"
        "/view – View your tasks\n"
        "/complete – Mark a task as completed\n"
        "/delete – Delete a task\n"
        "/help – Show this help message"
        "/cancel – Cancel adding a task\n\n",
        parse_mode="Markdown")