import os
from aiogram import executor
from handlers import dp
import game


os.system("CLS")

async def on_startup(_):
    print('Бот запущен')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)