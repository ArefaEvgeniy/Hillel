# Давайте создадим свой тип данных, который у себя будет сохранять строку.
# Это будет итерируемый тип данных, но итерироваться он будет следующим образом:
# в отличии от строк которые итерируются по буквам, наш объект будет
# итерироваться по словам, при чём каждое слово он будет возвращать с заглавной
# первой буквы и с приписными остальными, в не зависимости от того в каком виде
# это слово хранится в  нашей строке. При этом точки и запятые не выводятся.

values = 'Давайте создадим свой ТИП данных, который  у сЕбЯ будет сохранять строку.'


class MyIteration:
    def __init__(self, value):
        self.value = value
        self.count = len(value.split())
        self.current = 0

    def __next__(self):
        if self.current < self.count:
            data = self.value.split()[self.current]
            data = data.title().strip('.').strip(',')
            self.current += 1
            return data
        raise StopIteration


class MyClass:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
        else:
            self.data = ''
            if len(data) > 0:
                temp = []
                for item in data:
                    temp.append(str(item))
                self.data = ' '.join(temp)

    def __str__(self):
        return self.data

    def __iter__(self):
        return MyIteration(self.data)


a = MyClass(values)
for item in a:
    print(item)
