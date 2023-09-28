class MyDict(dict):
    def sum_values(self):
        res = 0
        for key in self:
            res += self[key] if isinstance(self[key], (int, float)) else 0
        return res


class MyClass(object):
    def __str__(self):
        return 'Hello'


a = MyDict()
print(a)
a.update({1: 1.1, 2: 2.5})
print(a)
print(a.sum_values())

b = MyClass()
print(b)
