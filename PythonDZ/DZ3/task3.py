# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(5):
    list[i] = round(list [i] - int(list[i]), 4)
print (list)

max = list[0]
min = list[0]

for i in range(5):
    if list[i] > max:
        max = list [i]
        
    if list[i] < min and list[i] !=0:
        min = list [i]
        
print(f'Разница между максимальным и минимальным значением дробной части элементов = {max-min}')