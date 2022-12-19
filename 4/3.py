""" Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности. 

Пример:
[1, 2, 2, 3] -> [1, 3] """

import os
os.system('CLS')

def find_singl_num(array: list) -> list:
    result = []
    for i in range(len(array)):
        if (array[i] not in array[i+1:]) and (array[i] not in array[:i]):
            result.append(array[i])
    print(result)
    
    
s = [10, 2, 1, 2, 2, 3, 3, 10, 30]

find_singl_num(s)