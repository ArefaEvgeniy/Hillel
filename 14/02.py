class MyList(list):
    def __add__(self, other):
        res = self.copy()
        for item in other:
            if item not in res:
                res.append(item)

        return MyList(res)

    def __sub__(self, other):
        res = self.copy()
        for item in other:
            if item in res:
                res.remove(item)

        return MyList(res)

    def __mul__(self, other):
        if isinstance(other, int):
            res = super().__mul__(other)
        else:
            res = []
            for item in other:
                if item in self:
                    res.append(item)

        return MyList(res)


a = MyList([1, 2, 3, 4])
b = MyList([5, 1, 5, 0, 2])

c = a + b
print(c)
print(type(c))

d = a - b
print(d)
print(type(d))

e = a * 3
print(e)
print(type(e))

f = a * b
print(f)
print(type(f))
