# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h = 0
#     a, b, c, d, e, h - рандом 

from random import randint

def input_number():
    while True:
        try:
            num = int(input('Введите размерность натуральной степени К: '))
            return num
        except:
            print('Ошибка ввода, попробуйте еще раз')

k = input_number()

for i in range(k, 0, -1):
    koef = randint(1, 101)
    if koef == 1:
        koef = ' '
    else:
        if i != 1:
            koef = f'{koef}*x^{i} +'
        else:
            koef = f'{koef}*x +'
    print(koef, end=' ')
print(f'{randint(1, 101)} = 0')