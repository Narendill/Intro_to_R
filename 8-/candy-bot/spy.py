from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def log(update: Update, context: CallbackContext) -> None:
    file = open('db.csv', 'a+')
    file.write(
        f'{update.effective_user.first_name}, {datetime.datetime.now()}, {update.effective_user.id}, {update.message.text}\n')
    file.close()