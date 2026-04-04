from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN
from handlers.start import start_command
from handlers.help import help_command
from handlers.add_task import conv_handler
from handlers.error import error
from handlers.view_tasks import view
from handlers.task_actions import complete
from handlers.task_actions import delete
from database import create_tables
from reminder_loader import load_existing_tasks
create_tables()

if __name__ == "__main__":
    #Create the bot application
    bot = ApplicationBuilder().token(TOKEN).connect_timeout(30).read_timeout(30).write_timeout(30).pool_timeout(30).build()
    load_existing_tasks(bot)
    #Register Commands
    bot.add_handler(CommandHandler('start', start_command))
    bot.add_handler(CommandHandler('help', help_command))
    bot.add_handler(conv_handler)
    bot.add_handler(CommandHandler('view', view))
    bot.add_handler(CommandHandler('complete', complete))
    bot.add_handler(CommandHandler('delete', delete))
    bot.add_error_handler(error)

    #Run the bot
    print('Bot is running...')
    bot.run_polling()
    