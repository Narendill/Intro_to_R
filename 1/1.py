""" Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет """

import os
os.system('CLS')

week_day = int(input('Input a number of the day: '))
if week_day >= 6:
    print('Weekend')
else:
    print('Work day')