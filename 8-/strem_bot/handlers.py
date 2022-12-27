from aiogram.types import Message
from config import dp
from aiogram.dispatcher.filters import Text
import game
import answers
from random import randint, choice
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


@dp.message_handler(commands=['set_total'])
async def set_total_candies(message: Message):
    if not game.check_game():
        max_total = message.text.split()
        if (len(max_total) > 1) and max_total[1].isdigit():
            game.set_max_total(int(max_total[1]))
            await message.reply(text=f'Максимальное количество конфет изменено на {max_total[1]}.')
            
        else:
            await message.reply(text='Этой командой можно настроить максимальное количество конфет. Введи /set_total и целое число. Например, /set_total 205')
    else:
        await message.reply(text='Данную настройку можно изменить только после окончания патрии.')


          
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
                
                # ____
                if take <= 10:
                    await message.answer(f'{choice(answers.little)}\n\n{name} взял {take} \U0001F36C и на столе осталось {game.get_total()} \U0001F36C. Ходит бот...')
                elif take >= 20:
                    await message.answer(f'{choice(answers.many)}\n\n{name} взял {take} \U0001F36C и на столе осталось {game.get_total()} \U0001F36C. Ходит бот...')
                else:
                    await message.answer(f'{choice(answers.other)} \U0001F607\n\n{name} взял {take} \U0001F36C и на столе осталось {game.get_total()} \U0001F36C. Ходит бот...')
                await bot_turn(message)
            elif take > game.get_total():
                await message.answer(f'{name}, разуй глаза! \U0001F440\nУ нас всего {game.get_total()} конфет!')
            
            else:
                await message.answer(f'Это по-твоему от 1 до 28???')
        else:
            await message.answer(f'Это чо такое? Число? \U0001F914')
            # pass
       
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
            await message.answer(f'{message.from_user.first_name} взял {take} \U0001F36C и победил! \U0001F451\nПоздравляю!\U0001F3C6\U0001F973\n\nЕсли хочешь еще потаскать конфеты, жмякай сюда: /new_game.')
            
        else:
            await message.answer(f'Ты проиграл, {message.from_user.first_name} \U0001F62A!\nБот взял {take} конфет \U0001F36C и победил!\U0001F916\n\nЕсли хочешь еще потаскать конфеты, жмякай сюда: /new_game.')
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