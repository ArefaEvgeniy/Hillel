class A():
    class_atr = 10

    def __init__(self, attr=0):
        self.attr = attr


a_1 = A()
a_2 = A(3)

print(f'a_1 attr: {a_1.attr}')
print(f'a_1 class_atr: {a_1.class_atr}')
print(f'a_2 attr: {a_2.attr}')
print(f'a_2 class_atr: {a_2.class_atr}')
print(a_1.__dict__)
print(a_2.__dict__)
A.class_atr = 33
print(f'a_1 class_atr: {a_1.class_atr}')
print(f'a_2 class_atr: {a_2.class_atr}')
a_1.class_atr = 99
print(f'a_1 class_atr: {a_1.class_atr}')
print(f'a_2 class_atr: {a_2.class_atr}')
print(a_1.__dict__)
print(a_2.__dict__)
print(f'A class_atr: {A.class_atr}')
