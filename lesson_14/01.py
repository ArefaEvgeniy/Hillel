# Створити свій клас даних на базі list(). Додати можливість віднімати та
# складати два об'єкти нового типу даних


class MyList(list):
    def __sub__(self, other):
        data = self[:]
        if isinstance(other, (int, str)):
            other = list((other,))
        for item in other:
            if item in data:
                data.remove(item)
        return MyList(data)


a = MyList((1, 2, 2, 3, 4, 5))
b = MyList((5, 2, 7))

c = a - b
print(c)
print(type(c))
print(a)
print(b)

print(a - 3)

# a_1 = [1, 2, 3, 4]
# print(a_1)
# a_2 = a_1[:]
# a_2.pop()
# print(a_1)
# print(a_2)
