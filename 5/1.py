""" Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 100 конфет. Играют два игрока
делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты
у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом" """

import os
import random
os.system('CLS')


def which_turn(player: int) -> int:
    if player == 1:
        print('The 2nd player turn.')
        return 2
    else:
        print('The 1st player turn.')
        return 1


def which_turn_bot(player: int) -> int:
    if player == 1:
        print('The bot\'s turn.')
        return 2
    else:
        print('The player turn.')
        return 1


def mistake():
    print()
    print('You can\'t get this quntity. Try again.')
    print()


print('There are 100 candies on the table.\nTwo players play making a move after each other.\n' +
      'The first move is determined by a draw.\nIn one move, you can pick up no more than 28 candies.\n' +
      'The player who made the last move and took the last candy wins.')
print()

candy = 100
max_size = 28
player_1_candy = 0  # Optional
player_2_candy = 0  # Optional

bot = input('Would you like to play with our bot (Y / N)? ')

try_s = 'Y'

while try_s == 'Y' or try_s == 'y':
    os.system('CLS')
    print('There are 100 candies on the table.\nTwo players play making a move after each other.\n' +
          'The first move is determined by a draw.\nIn one move, you can pick up no more than 28 candies.\n' +
          'The player who made the last move and took the last candy wins.')
    print('_____________________________________________')
    candy = 100
    max_size = 28
    player_1_candy = 0  # Optional
    player_2_candy = 0  # Optional

    if bot == 'N' or bot == 'n':
        print('The game for two players begins!')
        print()

        who_take_first = random.randint(1, 2)
        who_take_first = which_turn(who_take_first)

        print(f'There are {candy} candies now.')
        print()
        while candy > 0:
            take = int(input('How many candies do you want to take? '))
            if (0 < take <= max_size) and (0 < take <= candy):
                candy -= take

                # Optional
                if who_take_first == 1:
                    player_1_candy += take
                else:
                    player_2_candy += take

                print()
                print(f'---=== There are {candy} candies now ===---')

                if candy == 0:
                    print()
                    print(f'The player #{who_take_first} WINS!')
                    print('GAME OVER')
                    break
                print()
                who_take_first = which_turn(who_take_first)
            else:
                mistake()

        print('_____________________________________________')
        print(f'The 1st player took {player_1_candy} candies')
        print(f'The 2nd player took {player_2_candy} candies')
        print()
        try_s = input('Wold you like play again? (Y / N) ')
        print()
    else:
        print('The game for a player with a bot begins!')
        print()

        who_take_first = random.randint(1, 2)
        who_take_first = which_turn_bot(who_take_first)

        print(f'There are {candy} candies now.')
        print()
        while candy > 0:
            if who_take_first == 2 and (candy % (max_size + 1)) != 0:
                take = candy % (max_size + 1)
                print(f'The bot takes {take} candies.')
            elif who_take_first == 2 and (candy % (max_size + 1)) == 0:
                take = random.randint(1, min(max_size, candy))
                print(f'The bot takes {take} candies.')
            else:
                take = int(input('How many candies do you want to take? '))
            if (0 < take <= max_size) and (0 < take <= candy):
                candy -= take

                # Optional
                if who_take_first == 1:
                    player_1_candy += take
                else:
                    player_2_candy += take

                print()
                print(f'---=== There are {candy} candies now ===---')

                if candy == 0 and who_take_first == 1:
                    print()
                    print('The player WINS!')
                    print('GAME OVER')
                    break
                if candy == 0 and who_take_first == 2:
                    print()
                    print('The bot WINS!')
                    print('GAME OVER')
                    break
                print()
                who_take_first = which_turn_bot(who_take_first)
            else:
                mistake()

        print('_____________________________________________')
        print(f'The player took {player_1_candy} candies')
        print(f'The bot took {player_2_candy} candies')
        print()
        try_s = input('Wold you like play again? (Y / N) ')
        print()
