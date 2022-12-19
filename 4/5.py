""" Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов. """

from pathlib import Path
import os


os.system('CLS')

path_1 = Path('HW', '4', 'folder', 'task-5-1.txt')
path_2 = Path('HW', '4', 'folder', 'task-5-2.txt')

with open(path_1, 'r') as data:
    mnog_1 = data.readline().split()

with open(path_2, 'r') as data:
    mnog_2 = data.readline().split()

vse_x = []
for i in range(len(mnog_1)):
    for j in range(len(mnog_2)):
        if mnog_1[i] == '*' and mnog_1[i+1] not in vse_x:
            vse_x.append(mnog_1[i+1])
        if mnog_2[j] == '*' and mnog_2[j+1] not in vse_x:
            vse_x.append(mnog_2[j+1])

vse_x.sort(reverse=True)

new_mnogo = ''
for iks in vse_x:
    if iks in mnog_1 and iks in mnog_2:
        new_mnogo += str(int(mnog_1[mnog_1.index(iks)-2]) +
                         int(mnog_2[mnog_2.index(iks)-2])) + ' * ' + iks + ' + '
    elif iks in mnog_1 and iks not in mnog_2:
        new_mnogo += str(int(mnog_1[mnog_1.index(iks)-2])
                         ) + ' * ' + iks + ' + '
    else:
        new_mnogo += str(int(mnog_2[mnog_2.index(iks)-2])
                         ) + ' * ' + iks + ' + '


if mnog_1[mnog_1.index('=')-1].isdigit() and mnog_2[mnog_2.index('=')-1].isdigit():
    new_mnogo += str(int(mnog_1[mnog_1.index('=')-1]) +
                     int(mnog_2[mnog_2.index('=')-1]))
elif mnog_1[mnog_1.index('=')-1].isdigit():
    new_mnogo += str(int(mnog_1[mnog_1.index('=')-1]))
elif mnog_2[mnog_2.index('=')-1].isdigit():
    new_mnogo += str(int(mnog_2[mnog_2.index('=')-1]))

new_mnogo += ' = 0'

for i in mnog_1:
    print(i, ' ', end='')
print()
for i in mnog_2:
    print(i, ' ', end='')
print()
print()
print(new_mnogo)
