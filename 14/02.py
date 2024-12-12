class MyIter:
    def __init__(self, data: str):
        self.data = data.split()
        self.start = -1
        self.end = len(self.data)

    def __next__(self):
        self.start += 1
        if self.start < self.end:
            return self.data[self.start].title().replace(',', '').replace('.', '')
        raise StopIteration()


class My_Str(str):

    def __add__(self, other):
        return My_Str(f'{self} {other.capitalize()}')

    def __sub__(self, other):
        res = self
        for item in other:
            res = res.replace(item, '', 1)
        return My_Str(res)

    def __mul__(self, other):
        res = ''
        for item in self:
            res += item if item in other else ''
        return My_Str(res)

    def __iter__(self):
        return MyIter(self)


a = My_Str("Hello, world")
b = My_Str("new word")

c = a + b
print(c)
print(type(c))

d = a - b
print(d)

e = a * b
print(e)
print('-' * 100)

print(c)
for item in c:
    print(item)
