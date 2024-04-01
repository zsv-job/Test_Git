"""
Дополнить справочник возможностью копирования данных из одного файла в другой.
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
"""

from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'
new_file_name = 'phone2.csv'

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'имя': lst[0], 'фамилия': lst[1], 'телефон': lst[2]}
    res.append(obj)
    standart_write()
    # with open(file_name, 'w', encoding='utf-8', newline='') as data:
    #     f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
    #     f_w.writeheader()
    #     f_w.writerows(res)

def standart_write():
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def create_new_file(new_file_name):
    create_file(new_file_name)

def copy_rows(file_name, new_file_name):
    row_num = input("Введите номер записи:")
    res = read_file(file_name)
    for elem in res:
        if elem == row_num:

            copied_row = elem
            print(copied_row)
            write_file(new_file_name,copied_row)
            standart_write(new_file_name, copied_row)
            return copied_row
    print(elem)



def row_search(file_name):
    last_name = input("Введите фамилию для поиска:")
    res = read_file(file_name)
    for elem in res:
        # print(elem['фамилия'], last_name)
        if elem['фамилия'] == last_name:
            print(elem)
            break
    else:
        print("Фамилия",last_name ,"не найдена")



def main():
    while True:
        command = input("Введите комманду: ")
        if command == 'q':
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            print(*read_file(file_name))
        elif command == "c":
            create_file(new_file_name)
            copy_rows(file_name,new_file_name)
        elif command == "f":
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            row_search(file_name)



# main()
copy_rows(file_name,new_file_name)