# Создать объект-итератор, который при инициализации получает 2 значения:
# минимальное и максимальное. При каждом обращении он должен возвращать
# значения по порядку от минимального до максимального.


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.max = high

    def __next__(self):
        res = self.current
        self.current += 1
        if self.current <= self.max:
            return res
        raise StopIteration


a = Counter(3, 10)
try:
    print(f'Current: {a.current}')
    print(next(a))
    print(f'Current: {a.current}')
    print(next(a))
    print(f'Current: {a.current}')
    print(next(a))
    print(f'Current: {a.current}')
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration:
    print('Next data is absent')
