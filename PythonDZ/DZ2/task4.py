# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

try:
    num = int(input('Введите число N: '))
    sum = 0
    for i in range(2,num + 1,2):
        sum += i
    print (f'Сумма четных чисел {sum}')
except:
    print('Введите число')


