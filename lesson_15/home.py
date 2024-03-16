# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум
# додавання, віднімання, ділення, множення, зведення в ступінь та вилучення
# квадратного кореня. Обернути кожен метод у блок try/except і зробити обробку
# кількох винятків, як мінімум ділення на 0. Створити свій виняток, наприклад,
# зведення в негативний ступінь.


class Negative_degree(Exception):
    def __init__(self, message='Зведення у негативний ступінь'):
        super().__init__(message)


class Calculator(int):

    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        try:
            return Calculator(self.var + other)
        except TypeError:
            return 'Не можна складати цифри та літери!'

    def __sub__(self, other):
        try:
            return Calculator(self.var - other)
        except TypeError:
            return 'Не можна від цифри відібрати літери!'

    def __pow__(self, power, modulo=None):
        try:
                if power >= 0:
                    return Calculator(self.var ** power)
                else:
                    raise Negative_degree()
        except Negative_degree:
            return 'Зведення у негативний ступінь заборонено!'

    def __truediv__(self, other):
        try:
            return Calculator(self.var / other)
        except ZeroDivisionError:
            return 'Не можна ділити на нуль!'
        except TypeError:
            return 'Не можна ділити на літери!'
