class MyList(list):

    def __sub__(self, other):
        for item in other:
            if item in self:
                self.remove(item)
        return self

    def __add__(self, other):
        gena = MyList(self[:])
        gena.extend(other)
        return gena


a = MyList([1, 2, 3, 99])
b = MyList([5, 8, 99])

c = a + b
print(c)

a = a - b
print(a)

c = c - a
print(c)
