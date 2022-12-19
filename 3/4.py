""" Напишите программу, которая будет преобразовывать
десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

import os
os.system('CLS')


def dec_to_bin(n: int) -> str:
    n_in_bin = ''
    if n == 0:
        return '0'
    else:
        while n != 0:
            n_in_bin += str(n % 2)
            n = n // 2
        return n_in_bin[::-1]


print(dec_to_bin(45))
