from scheduler import send_reminder
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from database import get_all_tasks

def calculate_datetime(time_string):
    hour, minute = map(int, time_string.split(":"))

    now = datetime.now(ZoneInfo("Africa/Lagos"))

    reminder = datetime(
        now.year,
        now.month,
        now.day,
        hour,
        minute,
        tzinfo=ZoneInfo("Africa/Lagos")
    )

    if reminder < now:
        reminder += timedelta(days=1)

    return reminder

#reload all tasks
def load_existing_tasks(application):
    tasks = get_all_tasks()

    for task in tasks:
        task_id, user_id, name, description, time, duration, completed = task

        reminder_time = calculate_datetime(time)
        current_jobs = application.job_queue.get_jobs_by_name(str(task_id))
        for job in current_jobs:
            job.schedule_removal()
        application.job_queue.run_once(
            send_reminder,
            when=reminder_time,
            chat_id=user_id,
            name=str(task_id),
            data={"task_name": name}
        )