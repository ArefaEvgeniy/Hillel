# Создать свой тип данных, который у себя будет сохранять строку.
# Это будет итерируемый тип данных, но итерироваться он будет следующим образом:
# в отличии от строк которые итерируются по буквам, наш объект будет
# итерироваться по словам, при чём каждое слово он будет возвращать с заглавной
# первой буквы и с приписными остальными, в не зависимости от того в каком виде
# это слово хранится в  нашей строке. При этом точки и запятые не выводятся.

value = "Мама мыла РАМУ. Шла САША по шоссе и сасала сУШку."


class MyIter:
    def __init__(self, value):
        self.value = value.split()
        self.current = 0
        self.max = len(value.split())

    def __next__(self):
        if self.max > self.current:
            data = self.value[self.current].strip('.').strip(',')
            self.current += 1
            return data.title()
        raise StopIteration


class MyData:

    def __init__(self, data):
        self.data = str(data)

    def __str__(self):
        return self.data

    def __iter__(self):
        res = MyIter(self.data)
        return res


a = MyData(value)
print(a)

for item in a:
    print(item)
