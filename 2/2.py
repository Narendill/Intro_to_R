"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

import os
os.system('CLS')


def mult(n: int) -> list:
    lst = []
    proizv = 1
    for i in range(1, n+1):
        proizv *= i
        lst.append(proizv)
    print(lst)


n = int(input('Input a number: '))
mult(n)
