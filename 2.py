# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

length = int(input('Введите длинну массива: '))
new_list = []
for i in range(length):
    new_list.append(random.randint(0, 10))
print(new_list)
max_number = int(input('Введите максимальное число диапазона: '))
min_number = int(input('Введите минимальное число диапазона: '))
newer_list = []
for i in range(len(new_list)):
    if min_number <= new_list[i] <= max_number:
        newer_list.append(i)
print(f'Индексы массива, соответствующие диапазону: {newer_list}')
