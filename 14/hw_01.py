# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі
# додавання до групи більше 10-ти студентів, було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації. І
# обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при
# спробі додавання 11-го студента


class UserException(Exception):
    def __init__(self, message='У группі не може бути більше 10 студентів'):
        super().__init__(message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}.\nGender: {self.gender}\nAge: {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record book number: {self.record_book}"


class Group:

    def __init__(self, number, max_students_value=10):
        self.number = number
        self.max_students_value = max_students_value
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students_value:
            raise UserException()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
        else:
            return 'No, error!'

    def find_student(self, last_name):
        res = None
        for student in self.group:
            if student.last_name == last_name:
                res = student
                break
        return res

    def __str__(self):
        all_students = ';\n'.join([str(student) for student in gr.group])
        return f'Number:{self.number}\n{all_students} '


gr = Group('PD1')
try:
    gr.add_student(Student('Male', 22, 'Steve', 'Jobs', 'AN142'))
    gr.add_student(Student('Female', 25, 'Liza', 'Taylor', 'AN145'))
    gr.add_student(Student('Male', 24, 'Alex', 'Bingo', 'AN146'))
    gr.add_student(Student('Female', 18, 'Lina', 'Kostenko', 'AN147'))
    gr.add_student(Student('Male', 19, 'Alex', 'Yarem', 'AN148'))
    gr.add_student(Student('Female', 21, 'Inna', 'Demid', 'AN149'))
    gr.add_student(Student('Male', 19, 'Andrii', 'Yuskiv', 'AN150'))
    gr.add_student(Student('Female', 19, 'Ann', 'Sapiha', 'AN152'))
    gr.add_student(Student('Male', 23, 'Ivan', 'Kim', 'AN152'))
    gr.add_student(Student('Female', 24, 'Olena', 'Pchilka', 'AN153'))
    gr.add_student(Student('Male', 25, 'Bohdan', 'Shulha', 'AN154'))

except UserException as err:
    print(err)

print(gr)
print(f'У групі {len(gr.group)} студентів')
