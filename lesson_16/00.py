class AAA:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self, a=None, b=None):
        a = self.a if a is None else a
        b = self.b if b is None else b
        res = a + b
        return res


my_obj = AAA(1)
print(my_obj.add())
print(my_obj.add(5, 6))
