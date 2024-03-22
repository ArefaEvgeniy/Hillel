from date_base import DB


def main():
    data = DB()
    call_function = {1: data.input_data, 2: data.find, 3: data.file,
                     4: data.file, 5: data.file}
    while True:
        print("1. Ввести новий запис")
        print("2. Пошук у БД")
        print("3. Загрузити данні у БД з файла")
        print("4. Зберігти данні з БД у файл")
        print("5. Экспортувати данні у json формат")
        print('-' * 50)
        print("0. Вихід")
        choice = input("Що обираєте? ")

        if not choice.isdigit() or int(choice) > 5:
            print("Не вірний ввід")
            continue
        elif int(choice) == 0:
            break

        choice = int(choice)
        call_function[choice](choice)


if __name__ == "__main__":
    main()
