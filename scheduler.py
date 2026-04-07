from telegram.ext import ContextTypes
async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    task_name = job.data["task_name"]

    await context.bot.send_message(
        chat_id = job.chat_id,
        text=f"⏰ Reminder!\n\nYour task '{task_name}' is starting now!")