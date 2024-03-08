class A:
    attr_1 = 10

    def __init__(self, value=0):
        self.attr_2 = value


a_1 = A()
a_2 = A(5)
a_3 = A(-5)

print(a_1.__dict__)
print(a_2.__dict__)
print(a_3.__dict__)
print(a_1.attr_1)
print(a_2.attr_1)
print(a_3.attr_1)
A.attr_1 = 20
print(a_1.attr_1)
print(a_2.attr_1)
print(a_3.attr_1)

print('-' * 50)
a_1.attr_1 = 30
print(a_1.attr_1)
print(a_2.attr_1)
print(a_3.attr_1)
print(a_1.__dict__)
print(a_2.__dict__)
print(a_3.__dict__)
