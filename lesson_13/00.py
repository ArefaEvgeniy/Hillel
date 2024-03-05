class MyClass:

    def __init__(self):
        self.aa = '123'

    def set_aa(self, value):
        self.aa = value

    def get_aa(self):
        print(self.aa)


a_1 = MyClass()
a_1.get_aa()
