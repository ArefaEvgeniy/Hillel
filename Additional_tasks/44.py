# Реалізувати клас Counter, який представляє лічильник. Клас повинен
# підтримувати такі операції:
# - Збільшення значення лічильника на задане число (оператор +=)
# - Зменшення значення лічильника на задане число (оператор -=)
# - Перетворення лічильника на рядок (метод __str__)
# - Отримання поточного значення лічильника (метод __int__)
#
# Приклад використання:
# counter = Counter(5)
# counter += 3
# print(counter) # Результат: "Counter: 8"
# counter -= 2
# print(int(counter)) # Результат: 6


class Counter:
    def __init__(self, start):
        self.value = start

    def __add__(self, step):
        self.value += step
        return Counter(self.value)

    def __sub__(self, step):
        self.value -= step
        return Counter(self.value)

    def __str__(self):
        return f"Counter: {self.value}"

    def __int__(self):
        return self.value
