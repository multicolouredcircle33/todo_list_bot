from telegram import Update
from telegram.ext import ContextTypes
import database

async def complete(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text('Usage: /complete <task_id>\n'
                                        '<task_id> is the serial number of the task in the task list.\n' \
                                        'Click /view to see the task list.')
        return
    task_number  = context.args[0]
    if not task_number.isdigit():
        await update.message.reply_text('Task ID must be a number')
        return
    task_number = int(context.args[0]) - 1
    tasks = database.get_task(user_id)
    if task_number < 0 or task_number >= len(tasks):
        await update.message.reply_text("Invalid task number.")
        return
    task = tasks[task_number]
    task_id = task[0]
    database.mark_completed(user_id, int(task_id))
    current_jobs = context.job_queue.get_jobs_by_name(str(task_id))

    for job in current_jobs:
        job.schedule_removal()

    await update.message.reply_text(f'Task {task_number + 1} marked as completed✅\n'
                                    'Click /view to see your updated task list.')
    
async def delete(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text('Usage: /delete <task_id>\n'
                                        '<task_id> is the serial number of the task in the task list.\n' \
                                        'Click /view to see the task list.')
        return
    task_number  = context.args[0]
    if not task_number.isdigit():
        await update.message.reply_text('Task ID must be a number')
        return
    task_number = int(context.args[0]) - 1
    tasks = database.get_task(user_id)
    if task_number < 0 or task_number >= len(tasks):
        await update.message.reply_text("Invalid task number.")
        return
    task = tasks[task_number]
    task_id = task[0]
    database.delete_task(int(task_id), user_id)
    current_jobs = context.job_queue.get_jobs_by_name(str(task_id))
    for job in current_jobs:
        job.schedule_removal()

    await update.message.reply_text(f'Task {task_number + 1} deleted successfully✅\n'
                                    'Click /view to see your updated task list.')
    