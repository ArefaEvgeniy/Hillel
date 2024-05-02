class MyClass:
    TOTAL_OBJECTS = 0
    B = 0

    def __init__(self, a):
        self.a = a

    def set(self):
        MyClass.B = self.a


a_1 = MyClass(1)
a_2 = MyClass(22)
print(a_1.TOTAL_OBJECTS)
a_3 = MyClass(55)
a_4 = MyClass(0)

print(a_4.B)
a_2.set()
print(a_4.B)
print(a_1.B)
print(a_3.B)
