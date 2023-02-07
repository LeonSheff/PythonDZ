# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input("Введите любое вещественное число: ")

list_num = list(map(int, (i for i in number if i.isdigit())))

sum_digit = sum(list_num)

print(f"Сумма его цифр = {sum_digit}")