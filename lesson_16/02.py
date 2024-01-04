# Створити об'єкт-ітератор, який при ініціалізації приймає 2 значеня:
# мінімальне та максимальне. При кожному зверненні він повинен повертати
# значення по порядку від мінімального до максимального підіедений у куб мінус 1.


class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __next__(self):
        self.current += 1
        if self.current <= self.high:
            return (self.current ** 3) - 1
        raise StopIteration


a = Counter(2, 5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
