class MyStr(str):

    def __eq__(self, other):
        res = False
        if len(self) == len(other) and self.lower() in other.lower():
            res = True

        return res

    def __sub__(self, other):
        return MyStr(self[:len(self) - len(other)])

    def is_number(self):
        result = False
        if self.isdigit():
            result = True
        if '.' in self and self.count('.') == 1:
            result = True

        return result


a_1 = MyStr('45')
a_2 = MyStr('34.5567')
a_3 = MyStr('34.556.7')

print(a_1.title())
print(a_2.upper())

print(a_1 + a_2)

print(a_1.is_number())
print(a_2.is_number())
print(a_3.is_number())

b_1 = 'A'
b_2 = 'a'
print(b_1 == b_2)

c_1 = MyStr('BraD')
c_2 = MyStr('brad')
print('-' * 50)
print(c_1 == c_2)

print('-' * 50)
print(c_1 - 'rrr')
print(type(c_1 - 'rrr'))
