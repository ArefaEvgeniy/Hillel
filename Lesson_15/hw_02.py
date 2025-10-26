# Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання,
# віднімання та множення для екземплярів цього класу.
#
# https://www.google.com/search?q=Правильний+дріб
#
# class Fraction:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __mul__(self, other):
#         pass
#
#     def __add__(self, other):
#         pass
#
#     def __sub__(self, other):
#         pass
#
#     def __eq__(self, other):
#         pass
#
#     def __gt__(self, other):
#         pass
#
#     def __lt__(self, other):
#         pass
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"
#
# f_a = Fraction(2, 3)
# f_b = Fraction(3, 6)
# f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'
# f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 6, 18'
# f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'
#
# assert f_d < f_c  # True
# assert f_d > f_e  # True
# assert f_a != f_b  # True
# f_1 = Fraction(2, 4)
# f_2 = Fraction(3, 6)
# assert f_1 == f_2  # True
# print('OK')

import math


class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        """Спрощує дріб."""
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def __mul__(self, other):
        """Множить два дроби."""
        if isinstance(other, Fraction):
            new_a = self.a * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __add__(self, other):
        """Додає два дроби."""
        if isinstance(other, Fraction):
            new_a = self.a * other.b + other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __sub__(self, other):
        """Віднімає один дріб від іншого."""
        if isinstance(other, Fraction):
            new_a = self.a * other.b - other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __eq__(self, other):
        """Перевіряє на рівність два дроби."""
        if isinstance(other, Fraction):
            return self.a == other.a and self.b == other.b
        return False

    def __gt__(self, other):
        """Порівнює, чи більше поточний дріб за інший."""
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented

    def __lt__(self, other):
        """Порівнює, чи менший поточний дріб за інший."""
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented

    def __str__(self):
        """Повертає рядкове представлення дробу."""
        return f"Fraction: {self.a}, {self.b}"


# Перевірка
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

# Додавання
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6', str(f_c)  # Спрощений результат

# Множення
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3', str(f_d)  # Спрощений результат

# Віднімання
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6', str(f_e)  # Спрощений результат

# Порівняння
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

# Перевірка рівності дробів
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
print(f_c)
print(f_d)
print(f_e)
