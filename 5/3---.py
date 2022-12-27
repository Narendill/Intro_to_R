""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах. """

import os
os.system('CLS')

text = 'aaa bbb cccv'
print(text)
# print(len(text))

i = 0
count = 1

while i < len(text)-1:
    while text[i] == text[i+1]:
        count += 1
        i += 1
        if i == len(text)-2:
            if text[i] == text[i+1]:
                print(text[i], count+1)
                break
            else:
                print(print(text[i+1], 1))
                break
                
    print(text[i], count)
    count = 1
    i += 1
    

# print(result)