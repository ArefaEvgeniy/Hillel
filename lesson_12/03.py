class MyClass(str):
    def __sub__(self, other):
        return self.replace(other, '')

    def __str__(self):
        return str(len(self))


a_1 = MyClass('Red')
a_2 = MyClass('d')
print(a_1.upper())
print(a_2.upper())

print(a_1 - a_2)

print(a_1)
