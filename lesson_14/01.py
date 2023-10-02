# Створити свій клас даних на базі list(). Додати можливість віднімати та
# складати два об'єкти нового типу даних


class MyList(list):
    def __add__(self, other):
        max_len = len(self) if len(self) > len(other) else len(other)
        data = []
        for index in range(max_len):
            if len(self) > index and self[index] not in data:
                data.append(self[index])
            if len(other) > index and other[index] not in data:
                data.append(other[index])
        return MyList(data)

    def __sub__(self, other):
        data = self[:]
        for item in other:
            if item in data:
                data.remove(item)
            else:
                data.append(item)
        return MyList(data)


a = MyList([1, 3, 5])
b = MyList([1, 7])

c = a + b
print(c)
d = a - b
print(d)
print(type(d))
