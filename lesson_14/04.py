class MyClass:
    TOTAL_OBJECTS = 0

    def __init__(self, attr=0):
        self.attr = attr
        MyClass.TOTAL_OBJECTS += 1

    @classmethod
    def total_objects(cls):
        print(f"Total objects: {cls.TOTAL_OBJECTS}")


a_1 = MyClass()
a_2 = MyClass()
a_3 = MyClass()
a_4 = MyClass()
a_5 = MyClass()
a_5.TOTAL_OBJECTS = 99
a_5.total_objects()

MyClass.total_objects()
