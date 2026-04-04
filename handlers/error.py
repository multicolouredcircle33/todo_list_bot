from telegram import Update
from telegram.ext import ContextTypes

async def error(update, context):
    print(f'Update{update} caused error {context.error}')