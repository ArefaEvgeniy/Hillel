# Створіть клас «Прямокутник», у якого необхідно реалізувати два поля
# (ширина та висота) та кілька обов'язкових методів:
# Метод порівняння прямокутників за площею.
# Метод складання прямокутників (площа сумарного прямокутника повинна
# дорівнювати сумі площ прямокутників, які ви складаєте).
# Методи множення прямокутника на число n (це має збільшити площу базового
# прямокутника в n разів).
# У класі можуть бути створені додаткові (допоміжні методи)
#
# Декілька уточнень:
# Методи складання, множення, поділу тощо. обов'язково маємо повертати новий
# екземпляр класу Прямокутник! Для множення, додавання, порівняння, обов'язково
# потрібно перевизначати "магічні" методи. Для множення є вбудований метод mul
# Коли в результаті мат. дій створюєте новий екземпляр класу Прямокутник, то у
# цього екземпляру, перемноження сторін, має давати необхідну площу. Це теж
# важливо. Тобто, якщо Ви до прямокутника, у якого площа дорівнює 8, додаєте
# інший прямокутник з площею 18, необходимо створити новий прямокутник, площа
# якого дорівнює 26. Площа це довжина, помноженна на висоту. Значить необхідно
# підібрати сторони вновь створенного прямокутника таким чином, щоб вони давали
# необхідну площу!

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         pass
#
#     def __add__(self, other):
#         pass
#
#     def __mul__(self, n):
#         pass
#
#     def __str__(self):
#         pass
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        sum_area = self.get_square() + other.get_square()

        new_width = self.width

        new_height = sum_area // new_width

        while new_width * new_height != sum_area:
            new_width -= 1
            new_height = sum_area // new_width

        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_area = self.get_square() * n

        return Rectangle(self.width, new_area // self.width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(5, 18)
r2 = Rectangle(2, 17)
assert r1.get_square() == 90, 'Test1'
assert r2.get_square() == 34, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 124, 'Test3'

r4 = r3 * 4

assert r4.get_square() == 496, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(f'r1: {r1}')
print(f'r2: {r2}')
print(f'r3: {r3}')
print(f'r4: {r4}')
