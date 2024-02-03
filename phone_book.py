
import os
import time
import glob

def input_name():
    name = input("введите имя:")
    return name


def input_surname():
    surname = input("введите фамилию:")
    return surname


def input_patronymic():
    patronymic = input("введите отчество:")
    return patronymic


def input_phone():
    phone = input("введите номер телефона: ")
    return phone


def input_address():
    address = input("введите адрес: ")
    return address


def input_data():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    with open("phone_book.txt", "a", encoding="utf-8") as data:
        data.write(f"{name} {surname} {patronymic}\n{phone}\n{address}\n\n")


def print_data():
    os.system("cls")
    with open("phone_book.txt", "r", encoding="utf-8") as data:
        print(data.read())


def search_line():
    search = input("Введите значение поиска: ")
    found = False

    for filename in glob.glob("*.txt"):
        with open(filename, "r", encoding="utf-8") as data:
            lines = data.read().split("\n\n")[:-1]

            for i, line in enumerate(lines, start=1):
                time.sleep(1)
                if search in line:
                    print(f"Найдено в файле '{filename}' (строка {i}):")
                    print(line)
                    print()
                    found = True

    if not found:
        print("Совпадений не найдено.")


def copy_entry(source_file, destination_file, line_number):
    with open(source_file, "r", encoding="utf-8") as source:
        data = source.read().split("\n\n")[:-1]

        try:
            entry_to_copy = data[line_number - 1]
        except IndexError:
            print("Ошибка: введенный номер строки не существует.")
            return

        with open(destination_file, "a", encoding="utf-8") as dest:
            dest.write(f"{entry_to_copy}\n\n")

        print("Запись успешно скопирована.")


def interface():
    cmd = ""
    while cmd != "5":
        print("Выберите вариант действия:\n"
              "1. Запись\n"
              "2. Чтение\n"
              "3. Поиск\n"
              "4. Копирование записи\n"
              "5. Выход")

        cmd = input("Введите номер операции: ")
        while cmd not in ("1", "2", "3", "4", "5"):
            print("Ввод неверный!")
            cmd = input("Введите номер операции: ")

        if cmd == "1":
            input_data()
        elif cmd == "2":
            print_data()
        elif cmd == "3":
            search_line()
        elif cmd == "4":
            source_file = input(
                "Введите имя файла, из которого нужно скопировать: ")
            destination_file = input(
                "Введите имя файла, в который нужно скопировать: ")
            line_number = int(input("Введите номер строки для копирования: "))
            copy_entry(source_file, destination_file, line_number)

interface()
