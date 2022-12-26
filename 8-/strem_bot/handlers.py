from aiogram.types import Message
from config import dp
from aiogram.dispatcher.filters import Text
import game
import answers
from random import randint
import emoji


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}' + answers.rules)
        

@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    
    game.new_game()
    
    if game.check_game(): # Если True, делаем жеребьевку и начинаем играть.
        turn = randint(0, 1) # 0 - бот, 1 - игрок
        if turn:
            await message.answer(f'Волею судеб ты начинаешь!\U0001F52E')
            await player_turn(message)
        else:
            await message.answer(f'Волею судеб игру начинаю я!\U0001F52E')
            await bot_turn(message)
            
async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name},'
                         f' твой ход! Сколько возьмешь конфет \U0001F36C?')

@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if (0 < take < 29) and take <= game.get_total():
                game.take_candies(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(f'{name} взял {take} \U0001F36C и на столе осталось {game.get_total()} \U0001F36C. Ходит бот...')
                await bot_turn(message)
            else:
                await message.answer(f'Это по-твоему от 1 до 28???')
        else:
            pass
       
async def bot_turn(message: Message):
    total = game.get_total()
    if total <= 28:
        take = total
    else:
        take = randint(1, 28)
    game.take_candies(take)
    await message.answer(f'Бот взял {take} \U0001F36C и их осталось {game.get_total()}.')
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)

        
async def check_win(message, take: int, player: str):
    if game.get_total() <= 0:
        if player == 'player':
            await message.answer(f'{message.from_user.first_name} взял {take} \U0001F36C и победил! \U0001F451\nПоздравляю!\U0001F3C6\U0001F973')
            
        else:
            await message.answer(f'Ты проиграл, {message.from_user.first_name} \U0001F62A! Бот взял {take} конфет \U0001F36C и победил!')
        game.new_game()
        return True
    else:
        return False
# @dp.message_handler(commands=['start'])
# async def on_start(message: Message):
#     await message.answer(text=f'{message.from_user.first_name}, че нада?')
    
# @dp.message_handler(Text(equals=('100', '101')))
# async def on_hundred(message: Message):
#     await message.answer(text=f'Шеф, гляди, я поймал тебе цифр!')