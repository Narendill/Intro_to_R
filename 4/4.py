""" Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать
в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """

from pathlib import Path
import os
import random


os.system('CLS')

path = Path('HW', '4', 'folder', 'task-5-2.txt')

k = int(input('Input k: '))

with open(path, 'w') as data:
    mnogochlen = ''
    for i in range(k, 1, -1):
        power = random.randint(0, 100)
        if power != 0:
            mnogochlen += f'{power} * x^{i} + '
    power = random.randint(0, 100)
    if power != 0:
        mnogochlen += str(random.randint(0, 100))  
    mnogochlen += ' * x + ' 
    power = random.randint(0, 100)
    if power != 0:
        mnogochlen += str(random.randint(0, 100))
    mnogochlen += ' = 0'
    data.write(mnogochlen)






