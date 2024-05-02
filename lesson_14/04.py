class MyClass:
    TOTAL_OBJECTS = 0

    def __init__(self, a):
        self.a = a
        MyClass.TOTAL_OBJECTS += 1


# MyClass.TOTAL_OBJECTS = 3
a_1 = MyClass(1)
print(a_1.TOTAL_OBJECTS)
a_2 = MyClass(22)
a_3 = MyClass(55)
a_4 = MyClass(0)
print(a_1.TOTAL_OBJECTS)
a_5 = MyClass(0)
a_6 = MyClass(0)
a_7 = MyClass(0)
a_8 = MyClass(0)
a_9 = MyClass(0)
print(a_1.TOTAL_OBJECTS)
print(a_4.TOTAL_OBJECTS)
print(a_9.TOTAL_OBJECTS)
