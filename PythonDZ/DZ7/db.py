def data_collector():
    s_name = input('Введите фамилию: ')
    f_name = input('Введите имя: ')
    tele = input('Введите телефон: ')
    coment = input('Введите описание телефона (например рабочий): ')
    print()
    data = [s_name, f_name, tele, coment]
    return data

def db_save(data):
    file = 'file_column.txt'
    with open(file, 'a') as data: 
        data.write(f'Фамилия: {data[0]}; Имя: {data[1]}; Номер телефона: {data[2]}; Описание: {data[3]}\n')
        
    file = 'file_string.txt'
    with open(file, 'a') as data: 
        data.write(f'Фамилия: {data[0]}\n Имя: {data[1]}\n Номер телефона: {data[2]}\n Описание: {data[3]}\n\n')
        
def db_save(data):
    db_column = '\n'.join(data)
    db_column += '\n \n'
    with open('file_column.txt', 'a') as file:
        file.write(db_column)        
        
    db_string = '\n'.join(data)
    db_string += '\n \n'
    with open('file_string.txt', 'a') as file:
        file.write(db_string)   
        
        
def db_print(choise):
    if choise == 1:
        with open('file_column.txt', 'r') as file:
            for line in file:
                print(line, end='')
    if chise == 2:
        with open('file_string.txt', 'r') as file:
            for line in file:
                print(line, end= '')