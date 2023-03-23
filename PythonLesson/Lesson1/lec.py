# print('hello world') 





# типы данных и переменная
# int, float, boolean, str, list, None
# value = None

# print(type(value))

# print(type(a))
# print(type(b))
# print(type(value))
# s = 'hello \nworld'


#a = 123
#b = 1.23
#value =12334
#print(s) # вывод строки
#print(a, '-',b, '-', s)
#print('{} - {} - {}'.format(a,b,s))
#print(f'{a} - {b} - {s}')

#f = False
#print(f)

#list = ['1', '2', '3']
#col = [ 'hello', 1,2,3,4.5, True]
#print(list)
#print (col)

#print("Введите a");
#a = float(input())
#print("Введите b");
#b = float(input ())
#print (a,' + ', b, ' = ', a+b)
#print ('{} {}'.format(a,b))
#print (f'{a} {b}')

#a = 1.31231223
#b = 3
#c = round(a * b,7)
#print(c)

# Арифметические операции
# +, -, *, /, %, //, ** 
# унарный плюс и минус, 
# round для округления (), Сокращенные операции

#a = 3
#a += 5

#print (a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or -не путать с &, |, 
# кое что ещё : is , is not , in, not in
#gen

#a = 1 < 3 < 5 < 10

#f = [1,2,3,4]

#print (f)
#print (2 in f)

#is_odd = not f [0] % 2
#print ( is_odd)

# Управляющие конструкуции
# if =, if-else

#a = int (input('a = '))
#b = int (input('b = '))
#if a > b:
#    print(a)
#else:
#    print(b)

#username = input('Введите имя: ')
#if username == 'Маша':
#    print('Ура, это же МАША!')
#elif username == 'Марина':
#    print('Я так ждала Вас, Марина!')
#elif username == 'Ильнар':
#    print('Ильнар - топ)')
#else:
#    print('Привет, ', username)

# Управляющие конструкция    while

#original = 23
#inverted = 0
#while original !=0:
#    inverted = inverted * 10 + (original % 10)
#   original //= 10
#print(inverted)

# Управляющие конструкция   while-else

#original = 23
#inverted = 0
#while original !=0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#    print (original)
#else:
#    print("Пожалуй")
#    print("хватит)")

#print(inverted)

# Управляющая конструкция    for


#for i in 'qwe - rty':
#    print(i)

# Строки

#text = "съешь ещё этих мягких французких булок"
 
#print(len(text))                    #39
#print("ещё" in text)                #True
#print(text.isdigit())               #False
#print(text.islower())               #True
#print(text.replace('еще', 'ЕЩЁ'))   #

#for c in text:
#    print(c)
    
#Списки : Введение 
## list = list

#numbers = [1, 2, 3, 4, 5]
#print(numbers)
#ran = range(1, 6)
#print(type(ran))
#numbers = list(ran)
#print(type(numbers))

#print(numbers)
#numbers[0] = 10
#print(f'{len(numbers)} len')
#print(numbers)
#for i in numbers:
#    i *= 2
#    print(i)
#print(numbers)

colors = ['red', 'green', 'blue']

for e in colors:
    print (e)  # red green blue

for e in colors:
    print (e*2)  # redred greengreen blueblue

colors.append('gray')
print(colors == ['red', 'green', 'blue', 'gray'])
colors.remove('red')

del colors[0]









