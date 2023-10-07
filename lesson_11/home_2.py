# Прочитати збережений json-файл з попереднього завдання та записати дані на
# диск у csv-файл, першим стовпчиком буде ID (6-ти значне число, котре у
# попередньому завданні було ключем) і додавши новий стовпець "телефон".
# Крім цього, необхідно для кожного запису додати значення нового осередку
# “телефон”. Значення має бути заповнене випадковими цифрами.
# Назви стовпців будуть наступні:
# ID, Ім'я, Вік, Телефон.
# При цьому значення для перших трьох осередків необхідно дістати з json-файлу
# для кожного запису, а значення нового осередку "Телефон" сформувати.
#
# *Додаткове завдання не обов'язкове до виконання:
# формування значення комірки телефону має бути наступним:
# • не всі люди можуть мати номер телефону. Хто має номер телефону,
# а хто ні визначається автоматично випадковим чином.
# З ймовірністю 75% осіб має номер телефону, з ймовірністю 25% - ні;
# • є список можливих трьох перших цифр (операторів),
# Наприклад: ['095', '066', '098', '096', '050', '097']
# • при формуванні нового номера телефону перші 3 цифри вибираються випадковим
# чином зі списку можливих операторів, решта 7 цифр може бути будь-якими
# і формуються випадковим чином.
# Для виконання цього завдання необхідно розібратися з бібліотекою "random"


import json
import random
import csv


def get_phone_number():
    number = ""
    if random.randint(0, 3):
        operators = ['095', '066', '098', '096', '050', '097']
        number = random.choice(operators)
        for i in range(0, 7):
            number += str(random.randint(0, 9))

    return number


def read_data():
    with open('file_json.json') as file_json:
        result = json.load(file_json)

    return result


def prepare_data(data):
    result = [["ID", "Имя", "Возраст", "Телефон"]]
    for item_key in data:
        phone = get_phone_number()
        result.append([item_key, data[item_key][0], data[item_key][1], phone])

    return result


def write_data(data):
    with open("file_csv.csv", mode="w", encoding='utf-8') as w_file_csv:
        file_writer = csv.writer(w_file_csv, delimiter=",")
        for item in data:
            file_writer.writerow(item)


def main():
    data = read_data()
    new_data = prepare_data(data)
    write_data(new_data)


main()
