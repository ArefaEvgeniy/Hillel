class MyClass:

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.tatiana = 0

    # def sum(self, a, b):
    #     print(f'{a} + {b} + {self.age} = {a + b}')

    @staticmethod
    def sum(a, b):
        print(f'{a} + {b} = {a + b}')


num = MyClass(33, 'Oleg')
num.sum(4, 55)
num_2 = MyClass(11, 'Katia')
num_2.sum(4, 55)

MyClass.sum(66, 77)
