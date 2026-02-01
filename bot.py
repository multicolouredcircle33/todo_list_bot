from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN

from handlers.start import start_command
from handlers.help import help_command

if __name__ == "__main__":
    #Create the bot application
    app = ApplicationBuilder().token(TOKEN).build()
    #Register Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #Run the bot
    print('Bot is running...')
    app.run_polling()