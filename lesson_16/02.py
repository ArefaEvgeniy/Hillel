# Створити об'єкт-ітератор, який при ініціалізації приймає 2 значеня:
# мінімальне та максимальне. При кожному зверненні він повинен повертати
# значення по порядку від мінімального до максимального.


class Counter:
    def __init__(self, low, high):
        if low > high:
            low, high = high, low
        self.current = low - 1
        self.high = high

    def __next__(self):
        self.current += 1
        if self.current <= self.high:
            return self.current
        raise StopIteration


a = Counter(2, 5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
