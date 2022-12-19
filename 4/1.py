""" Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ """

import os
import math
os.system('CLS')


def accuracy(d: str) -> float:
    d = len(d.split('.')[1])
    print(round(math.pi, d))


d = input('Enter the accuracy: ')
accuracy(d)
