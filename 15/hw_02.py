# У цьому завданні Вам необхідно зробити дві речі на підставі попереднього ДЗ.
# До класу Студента необхідно додати метод порівняння. Порівнювати можна за
# тими рядками, які повертає метод str Для того, щоб спрацювала ця перевірка:
#
# assert gr.find_student('Jobs') == st1
# Рознесіть класи, які використовували під час виконання завдання про групу
# студентів за модулями. Переконайтеся у працездатності проекту – створіть
# окремо файл main.py, у якому необхідно імпортувати потрібні класи та
# запустити код перевірки.
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
# assert gr.find_student('Jobs2') is None
#
# gr.delete_student('Taylor')
# print(gr) # Only one student
# Результат оформить у вигляді zip-архіву, в якому будуть зібрані всі необхідні модулі.
#
# Якщо при спробі додавання студента до групи ви побачите помилку
# self.group.add(student)
# TypeError: unhashable type: 'Student'
# то додайте до класу студента метод hash
#
# def __hash__(self):
#     return hash(str(self))

