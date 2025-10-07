# Створіть клас, що описує людину (створіть метод, що виводить інформацію про
# людину). На його основі створіть клас Студент (перевизначте метод виведення
# інформації). Створіть клас Група, екземпляр якого складається з об'єктів
# класу Студент. Реалізуйте методи додавання, видалення студента та метод
# пошуку студента на прізвище. Метод пошуку студента повинен повертати саме
# екземпляр класу Студент, якщо студент є у групі, інакше - None.
#
# У методі видалення, використовуйте результат методу пошуку.
# Тобто, потрібно скомбінувати ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
#
# Нижче наведені заготовки, які необхідно доповнити.

# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         pass
#
#     def __str__(self):
#         pass
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         pass
#
#     def __str__(self):
#         pass
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         pass
#
#     def find_student(self, last_name):
#         pass
#
#     def __str__(self):
#         all_students = ''
#         ...
#         return f'Number:{self.number}\\n {all_students} '
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!
