class MyStr(str):
    def __mul__(self, other):
        return (self + str(other)) + str(len(other))


a_1 = 1
a_2 = 2
b_1 = MyStr('red')
b_2 = MyStr('e')

print(a_1 + a_2)
print(b_1 + b_2)
print(a_1 - a_2)
print(b_1 * b_2)
