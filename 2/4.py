""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.
 """
import os
os.system('CLS')


def fill_array(n: int, position: list):
    array = []
    for i in range(-n, n+1):
        array.append(i)
    print(array)

    if int(position[0]) <= len(array) and int(position[1]) < len(array):
        print(array[int(position[0])] * array[int(position[1])])
    else:
        print('Your position is not correct.')


n = int(input('Input N: '))
position = input('Input position: ').split()

fill_array(n, position)
