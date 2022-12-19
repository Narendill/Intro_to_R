""" Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

import os
os.system('CLS')


def mult_array(array: list) -> list:
    new_array = []
    if len(array) % 2 == 0:
        for i in range(int(len(array) / 2)):
            new_array.append(array[i] * array[-i-1])
    else:
        for i in range(int(len(array) / 2) + 1):
            new_array.append(array[i] * array[-i-1])
    return new_array


array_1 = [2, 3, 4, 5, 6]
array_2 = [2, 3, 5, 6]

print(mult_array(array_1))
print(mult_array(array_2))
