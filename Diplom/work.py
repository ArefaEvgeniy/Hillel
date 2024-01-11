import pickle
from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, middle_name, birth_date, death_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def calculate_age(self, current_date):
        # Отримуємо рік народження
        birth_date = datetime.strptime(self.birth_date, '%d.%m.%Y')
        # Отримуємо поточний рік
        current_date = datetime.now()

        # Обчислюємо вік
        age = current_date.year - birth_date.year

        # Перевіряємо, чи вже відзначився день народження цього року
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def __str__(self):
        if self.death_date:
            return f"{self.last_name} {self.first_name} {self.middle_name}, {self.calculate_age(self.death_date)} років, " \
                   f"{self.gender}. Народився {self.birth_date}. Помер: {self.death_date}."
        else:
            return f"{self.last_name} {self.first_name} {self.middle_name}, {self.calculate_age(self.birth_date)} років, " \
                   f"{self.gender}. Народився {self.birth_date}."


# Функція для збереження даних у файл
def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


# Функція для завантаження даних з файлу
def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


# Функція для введення нових даних про людину
def input_person_data():
    first_name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    middle_name = input("Введіть по-батькові (натисніть Enter, якщо відсутнє): ")
    birth_date = input("Введіть дату народження (у форматі ДД.ММ.РРРР): ")
    death_date = input("Введіть дату смерті (у форматі ДД.ММ.РРРР, або натисніть Enter, якщо відсутня): ")
    gender = input("Введіть стать (m - чоловік, f - жінка): ")

    return Person(first_name, last_name, middle_name, birth_date, death_date, gender)


# Функція для пошуку за введеним рядком
def search_people(people, search_str):
    found_people = []
    for person in people:
        if search_str.lower() in (person.first_name.lower(), person.last_name.lower(), person.middle_name.lower()):
            found_people.append(person)

    return found_people


# Головна програма
if __name__ == "__main__":
    data_filename = 'people_data.pkl'
    people_data = load_data(data_filename)

    while True:
        print("\nМеню:")
        print("1. Ввести нові дані про людину")
        print("2. Пошук людини")
        print("3. Зберегти дані у файл")
        print("4. Завантажити дані з файлу")
        print("5. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            person = input_person_data()
            people_data.append(person)
            print("Дані про людину додані успішно.")

        elif choice == '2':
            search_str = input("Введіть рядок для пошуку: ")
            found_people = search_people(people_data, search_str)
            if found_people:
                for person in found_people:
                    print(str(person))
            else:
                print("Людина не знайдена.")

        elif choice == '3':
            save_data(people_data, data_filename)
            print("Дані збережені у файл.")

        elif choice == '4':
            people_data = load_data(data_filename)
            print("Дані завантажені з файлу.")

        elif choice == '5':
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
