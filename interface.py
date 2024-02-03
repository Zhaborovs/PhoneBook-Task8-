def run_interface():
    from functions import input_data, print_data, search_line, copy_entry

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
