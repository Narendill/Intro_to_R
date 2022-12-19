""" Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением
дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

import os
os.system('CLS')

def min_max_array_1(array: list) -> float:
    new_array = []
    for i in array:
        if type(i) != int:
            number = '0.' + str(i).split('.')[1]
            new_array.append(float(number))
    diff = max(new_array) - min(new_array)
    return diff

# OR
def min_max_array_2(array: list) -> float:
    new_array = []
    for i in array:
        if i - int(i) != 0:
            new_array.append(i - int(i))
    diff = max(new_array) - min(new_array)
    return round(diff, 4)



array_1 = [1.1, 1.2, 3.1, 5, 10.01]

print(min_max_array_1(array_1))
print(min_max_array_2(array_1))