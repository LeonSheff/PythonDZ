def action():
    print('Если вы хотите записать информацию в справочник введите - 1\nЕсли вы хотите считать информацию из справочника введите - 2\nЕсли вы хотите выйти из программы - 3')
    choise = int(input())
    print()
    return choise

def db_view():
    print(f'В каком виде вы хотите считать данные?')
    print('Введите 1 для выбора:\nФамилия\nИмя\nТелефон\nОписание\n')
    print('Введите 2 для выбора:\nФамилия\nИмя\nТелефон\nОписание\n')
    choise = int(input())
    print()
    return choise