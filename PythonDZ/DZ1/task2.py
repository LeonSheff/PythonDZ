# 2. Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = int(input('введите х(0 или 1) ')), int(input('введите y(0 или 1) ')), int(input('введите z(0 или 1) '))
count = 0
for i in range(1, 9):
    if (not(x == 1 or y == 1 or z == 1) == (not x == 1 and not y == 1 and not z == 1)):
        count += 1
    else:
       break
    if (i == 1):
        x = 0
        y = 0
        z = 1
    elif (i == 2):
       x = 0
       y = 1
       z = 0
    elif (i == 3):
       x = 0
       y = 1
       z = 1
    elif (i == 4):
       x = 1
       y = 0
       z = 0
    elif (i == 5):
       x = 1
       y = 0         
       z = 1
    elif (i == 6):
        x = 1
        y = 1
        z = 0
    else:
        x = 1
        y = 1
        z = 1
if count == 8:
     print('логическое выражение истинно')
else:
     print('логическое выражение не истинно')