""" Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} """

import os
os.system('CLS')

n = 6
summa = 0
lst = []
for i in range(1, n+1):
    summa += ((1 + 1 / i) ** i)
    lst.append(summa)
    print(i, summa)

print(lst)
