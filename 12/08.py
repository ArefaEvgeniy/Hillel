class String(str):
    def __add__(self, other):
        return String(super().__add__(other))
        # return String(str(self) + str(other))

    def __sub__(self, other):
        return String(self.replace(other, '', 1))


a = String('Hello, ')
b = String('world')
c = String('llo')

d = a + b + c
print(d)
print(type(d))
print(d - c - 'wor')
