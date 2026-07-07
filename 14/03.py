class MyStr(str):
    def __sub__(self, other):
        if isinstance(other, str):
            result = self
            for char in other:
                result = result.replace(char, "", 1)
            return MyStr(result)
        return NotImplemented


a1 = MyStr("Hello, world!")
print(a1)
print(type(a1))
print(a1.lower())
print(a1.isdigit())

a2 = MyStr("Hello ")
a3 = MyStr("world!")
print(type(a2))
print(a2 + a3)
print(a2 - a3)
