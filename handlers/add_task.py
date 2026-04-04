from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, ConversationHandler, filters, CommandHandler
from database import save_task
from datetime import datetime, timedelta
from scheduler import send_reminder
from zoneinfo import ZoneInfo
TASK_NAME, TASK_DESC, TASK_TIME, TASK_DURATION = range(4)
async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('What is the name of the task: ')
    return TASK_NAME
async def get_task_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['task_name'] = update.message.text
    await update.message.reply_text('Give a short description of the task: ')
    return TASK_DESC
async def get_task_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['task_desc'] = update.message.text
    await update.message.reply_text('What time do you want to start(24hr format HH:MM): ')
    return TASK_TIME
async def get_task_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['task_time'] = update.message.text
    await update.message.reply_text(f'How long will it take(in minutes)?')
    return TASK_DURATION
async def get_task_duration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['task_duration'] = update.message.text
    user_id = update.effective_user.id
    name = context.user_data["task_name"]
    desc = context.user_data["task_desc"]
    time = context.user_data["task_time"]
    duration = context.user_data["task_duration"]
    task_id = save_task(user_id, name, desc, time, duration)

    hour, minute = map(int, time.split(":"))

    now = datetime.now(ZoneInfo("Africa/Lagos"))

    reminder_time = datetime(
        now.year,
        now.month,
        now.day,
        hour,
        minute,
        tzinfo=ZoneInfo("Africa/Lagos")
    )

    if reminder_time < now:
        reminder_time = reminder_time + timedelta(days=1)
    # --- schedule reminder ---
    print("Scheduling reminder for:", reminder_time)
    
    context.job_queue.run_once(
        send_reminder,
        when = reminder_time,
        chat_id = user_id,
        name = str(task_id),
        data = {
            "task_name": name
        }
    )

    await update.message.reply_text(
        f"✅ Your task has been saved!\n\n"
        f"📌 Name: {name}\n"
        f"📝 Description: {desc}\n"
        f"⏰ Time: {time}\n"
        f"⏳ Duration: {duration} minutes"
    )
    return ConversationHandler.END

# ----- CANCEL COMMAND -----#
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Task creation cancelled.")
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("add", add_task)],
        states={
            TASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_task_name)],
            TASK_DESC: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_task_desc)],
            TASK_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_task_time)],
            TASK_DURATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_task_duration)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
)
