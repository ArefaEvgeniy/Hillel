# Создать объект-итератор, который при инициализации получает 2 значения:
# минимальное и максимальное. При каждом обращении он должен возвращать
# значения по порядку от минимального до максимального.


class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.max = high

    def __next__(self):
        self.current += 1
        if self.current <= self.max:
            return self.current
        raise StopIteration


a = Counter(2, 5)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for item in a:
    print(item)
