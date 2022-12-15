""" Напишите программу, которая принимает на вход
координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
и выдаёт номер четверти плоскости, в которой находится эта точка
(или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

import os
os.system('CLS')

x = int(input('X: '))
y = int(input('Y: '))

if x == 0 and y == 0:
    print('Your input is not correct.')
elif x == 0:
    print('Your point is on Oy.')
elif y == 0:
    print('Your point is on Ox.')
elif x > 0 and y > 0:
    print('Your point is I quater.')
elif x < 0 and y > 0:
    print('Your point is II quater.')
elif x < 0 and y < 0:
    print('Your point is III quater.')
else:
    print('Your point is IV quater.')
