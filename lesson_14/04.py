class MyClass:
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS += 1

    @classmethod
    def decrim_total(cls):
        cls.TOTAL_OBJECTS += 1

    @classmethod
    def total_objects(cls):
        print('Total objects:', cls.TOTAL_OBJECTS)


class MyClass2(MyClass):
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass2.TOTAL_OBJECTS += 1


a_1 = MyClass()
a_1.decrim_total()
a_2 = MyClass()
a_2.decrim_total()
a_1.total_objects()

b_1 = MyClass2()
b_1.decrim_total()
b_2 = MyClass2()
b_2.decrim_total()
b_1.total_objects()

print(MyClass.TOTAL_OBJECTS)
print(MyClass2.TOTAL_OBJECTS)
