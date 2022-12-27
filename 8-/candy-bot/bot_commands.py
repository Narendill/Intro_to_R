from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
import emoji




async def hi_command(update: Update, context: CallbackContext) -> None:
    log(update, context)
    await update.message.reply_text(f'Привет, дорогой {update.effective_user.first_name}! \U00002764\nХочешь поиграть со мной в конфетки? \U0001F36C')


async def help_command(update: Update, context: CallbackContext) -> None:
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')


async def time_command(update: Update, context: CallbackContext) -> None:
    log(update, context)
    await update.message.reply_text(f'Время: {datetime.datetime.now().time()}')


async def sum_command(update: Update, context: CallbackContext) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    try:
        x = int(items[1])
        y = int(items[2])
        await update.message.reply_text(f'{x} + {y} = {x + y}')
    except ValueError:
        await update.message.reply_text(f'Введи два числа через пробел! Например: /sum 11 55')
    except IndexError:
        await update.message.reply_text(f'Введи два числа через пробел! Например: /sum 11 55')
