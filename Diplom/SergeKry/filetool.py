from person import Person
import csv


def export_file(path):
    heading_row = ["Прізвище", "Ім'я", "По батькові", "Дата народження", "Дата смерті", "Стать", "Вік"]
    if path:
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(heading_row)
            for item in Person.PERSONS:
                writer.writerow(item[0:7])
        return 'Файл збережено'


def import_file(path):
    if path:
        try:
            with open(path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                data = []
                for row in reader:
                    data.append(row)
                for person in data[1:]:
                    first_name = person[1]
                    birth_date = Person.parse_date(person[3])
                    gender = person[5]
                    second_name = person[2]
                    last_name = person[0]
                    death_date = Person.parse_date(person[4]) if person[4] != '' else None
                    Person(first_name, birth_date, gender, second_name, last_name, death_date)
            return 'Дані імпортовані'
        except Exception:
            return 'Неможливо завантажити'
