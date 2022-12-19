""" Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

import os
os.system('CLS')


def sum_odd(array: list) -> int:
    sum = 0
    for i in range(1, len(array), 2):
        sum += array[i]
    return sum


array = [2, 3, 5, 9, 3]
print(sum_odd(array))
