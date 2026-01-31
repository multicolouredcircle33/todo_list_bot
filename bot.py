from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from config import TOKEN
#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text( "👋 Hi! I'm your To-Do List Bot.\n\n"
        "I can help you add tasks, remind you when it's time, "
        "and manage your daily activities.\n\n"
        "Type /help to see what I can do.")
if __name__ == "__main__":
    #Create the bot application
    app = ApplicationBuilder().token(TOKEN).build()
    #Register Commands
    app.add_handler(CommandHandler('start', start_command))
    #Run the bot
    print('Bot is running...')
    app.run_polling()