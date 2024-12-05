class My_Str(str):

    def __sub__(self, other):
        return self.replace(other, '', 1)


a = My_Str('Hello, world')
b = My_Str('llo')
print(type(a))

print(a + b)
print(a - b)
print(a - 'l')
