""" Напишите программу, которая принимает на вход
вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11 """

import os
os.system('CLS')


def sum_digits_1(number: str):
    number_split = number.split('.')
    number_join = ''.join(number_split)
    summa = 0
    for digit in number_join:
        summa += int(digit)
    print(f'summa = {summa}')

# OR


def sum_digits_2(number: str):
    summa = 0
    for digit in number:
        if digit != '.':
            summa += int(digit)
    print(f'summa = {summa}')


n = input('Input a number: ')
sum_digits_1(n)
sum_digits_2(n)
