""" Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат. """

import os
os.system('CLS')

x = input('X: ')
y = input('Y: ')
z = input('Z: ')

if not (x or y or z) == ((not x) and (not y) and (not z)):
    print(True)
else:
    print(False)