""" Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y). """

import os
os.system('CLS')

quater = int(input('Quater: '))

if quater == 1:
    print('x: (0; +inf), y: (0; +inf)')
elif quater == 2:
    print('x: (-inf; 0), y: (0; +inf)')
elif quater == 3:
    print('x: (-inf; 0), y: (-inf; 0)')
else:
    print('x: (0; +inf), y: (-inf; 0)')