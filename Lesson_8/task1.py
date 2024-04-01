from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'


def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер')
    return [first_name, last_name, phone_number]


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
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(res)


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


main()
