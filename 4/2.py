""" Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N. """

import os
os.system('CLS')


# def is_prime(num: int) -> bool:
#     for i in range(2, int(n**0.5+1)):
#         if n % i == 0:
#             return False
#     return True


def prime_div(num: int) -> list:
    array = []
    for i in range(2, int(num**0.5+1)):
        while num % i == 0:
            array.append(i)
            num = num / i
    if num != 1:
        array.append(num)
    return array


n = int(input('Input your number: '))
print(prime_div(n))

mult = 1
for i in prime_div(n):
    mult *= i
print(f'mult = {mult}')
