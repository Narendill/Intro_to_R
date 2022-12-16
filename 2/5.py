""" Реализуйте алгоритм перемешивания списка. """

import os
os.system('CLS')


array = [1, 2, 3, 4, 5, 6, 7, 8]


def mix_array(array: list) -> list:
    for j in range(2):
        i = 0
        while i < len(array) - 1:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            i += 2
    
        i = 0
        while i < len(array) - 2:
            temp = array[i]
            array[i] = array[i+2]
            array[i+2] = temp
            i += 3
    print(array)


mix_array(array)
