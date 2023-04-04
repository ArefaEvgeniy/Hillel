class MyStr(str):
    def __mul__(self, other):
        return MyStr(f'{self}{self}{str(other)}{str(other)}')


a = MyStr('wer')
print(a)
print(a.title())
print(a * 'AD')
print(a * 78)
b = MyStr('RET')
print(a * b)
print(str(type(a * b)))
