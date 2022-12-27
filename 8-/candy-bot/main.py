import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

os.system('CLS')

app = ApplicationBuilder().token(
    "530330700:AAHK5WAmyb8uiBnJFiUZFX_SIVCYJ_dYYFA").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')

app.run_polling()
