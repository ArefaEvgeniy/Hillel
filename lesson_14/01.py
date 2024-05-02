class MyList(list):
    def __add__(self, other):
        data = []
        for item in self:
            if item not in data:
                data.append(item)
        for item in other:
            if item not in data:
                data.append(item)
        return MyList(data)

    def __sub__(self, other):
        data = self[:]
        for item in other:
            if item in data:
                data.remove(item)
        return MyList(data)


a_1 = MyList((1, 2, 'e', 'r', 'red', 'e', 1, 3, 0))
a_2 = MyList((0, 'red', 'white', True, 1, 0))

a_3 = a_1 + a_2
a_4 = a_1 - a_2
print(a_3)
print(type(a_3))
print(a_4)
print(type(a_4))
