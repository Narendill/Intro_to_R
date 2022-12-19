""" Задайте число. Составьте список чисел Фибоначчи
в том числе для отрицательных индексов.

Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """

import os
os.system('CLS')


def fibo(k: int) -> list:
    array = [0, 1]
    f_1 = 0
    f_2 = 1
    if k == 0:
        return [0]
    elif k == 1:
        return array
    else:
        for i in range(0, k-1):
            next_fi = f_1 + f_2
            array.append(next_fi)
            f_1 = f_2
            f_2 = next_fi

        array_new = []
        for i in range(1, len(array)):
            array_new.insert(0, (-1)**(i+1)*array[i])
        for i in array:
            array_new.append(i)
        return array_new


print(fibo(3))
