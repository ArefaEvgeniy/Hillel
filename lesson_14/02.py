class MyClass(object):

    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print(f"Tatol objects: {cls.TOTAL_OBJECTS}")


a_1 = MyClass()
a_1.total_objects()
MyClass.total_objects()
a_2 = MyClass()
MyClass.total_objects()
a_3 = MyClass()
MyClass.total_objects()

