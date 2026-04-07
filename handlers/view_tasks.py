from database import get_task
from telegram import Update
from telegram.ext import ContextTypes

async def view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tasks = get_task(user_id)

    if not tasks:
        await update.message.reply_text('You have no tasks.')
        return  

    message = ""
    for index, task in enumerate(tasks, start=1):
        task_id, name, desc, time, duration, completed = task
        status = "✅" if completed else "❌"
        message += f"{status} {index}. {name} at {time} ({duration} mins)\n"

    await update.message.reply_text(message)