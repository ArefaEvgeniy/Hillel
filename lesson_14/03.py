class A:
    class_atr = 10

    def __init__(self, atr=0):
        self.atr = atr


a = A()
print('A.class_atr', A.class_atr)
print('a.atr', a.atr)
print('a.__dict__', a.__dict__)
print('-' * 50)

b = A(7)
print('A.class_atr', A.class_atr)
print('a.atr', a.atr)
print('b.atr', b.atr)
print('-' * 50)

c = A(5)
print('A.class_atr', A.class_atr)
print('a.atr', a.atr)
print('b.atr', b.atr)
print('c.atr', c.atr)
print('a.class_atr', a.class_atr)
print('-' * 50)

c.atr = 22

A.class_atr = 20
print('a.atr', a.atr)
print('b.atr', b.atr)
print('c.atr', c.atr)
print('a.class_atr', a.class_atr)
print('b.class_atr', b.class_atr)
print('c.class_atr', c.class_atr)

print('-' * 50)
print('a.__dict__', a.__dict__)
a.class_atr = 33
print('a.__dict__', a.__dict__)
print('b.__dict__', b.__dict__)
print('c.__dict__', c.__dict__)
print('a.class_atr', a.class_atr)
print('b.class_atr', b.class_atr)
print('c.class_atr', c.class_atr)

