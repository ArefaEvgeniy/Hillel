import json
import pickle


class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_age(self):
        age = self.age
        if self.age < 18:
            age = self.age + 2
        elif self.age > 30:
            age = self.age - 5

        return age


if __name__ == "__main__":
    p_1 = Person('Tetiana', 'Lisko', 25)
    p_2 = Person('Genadiy', None, 33)
    p_3 = Person('Bob', 'Krud', 12)

    print(p_3.get_age())

    data = []
    for person in (p_1, p_2, p_3):
        per_data = {}
        per_data.update({'name': person.name})
        per_data.update({'surname': person.surname})
        per_data.update({'age': person.age})
        data.append(per_data)

    with open('data.json', 'w') as file:
        json.dump(data, file)

    with open('data.pkl', 'wb') as file:
        pickle.dump((p_1, p_2, p_3), file)
