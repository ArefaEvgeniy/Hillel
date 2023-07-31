class MyClass(str):

    CLASS_ARG = 123
    arg_a = None
    arg_b = None

    def __init__(self, my_arg):
        self.my_arg = my_arg

    def __add__(self, other):
        return f'{self}{str(other)}'

    def __int__(self):
        negative = False
        value = self[:]
        if self.startswith('-') and len(self) > 1:
            negative = True
            value = self[1:]
        new_value = ''
        for item in value:
            if item.isdigit():
                new_value += item
        new_value = f'-{new_value}' if new_value and negative else new_value
        return 0 if not new_value else int(new_value)

    @staticmethod
    def static_method(arg_1, arg_2, arg_g=None):
        if isinstance(arg_1, int) and isinstance(arg_2, int):
            return arg_1 + arg_2
        else:
            return arg_g

    @classmethod
    def class_method(cls, arg_1, arg_2):
        if isinstance(arg_1, int) and isinstance(arg_2, int):
            cls.CLASS_ARG = cls.static_method(arg_1, arg_2)
        return cls.CLASS_ARG

    def general_method(self, arg_1):
        self.arg_a = arg_1 if arg_1 else MyClass.CLASS_ARG
        self.arg_b = self.my_arg


a = MyClass('4ddrt5-7gjyj6678f33,.,fty560')
print(a + 123)
print(int(a))
print(type(int('6667')))

print('-' * 50)

a = MyClass(10)
a.general_method(None)
# MyClass.general_method('dd')

print(a.static_method(1, 2, MyClass.CLASS_ARG))
print(MyClass.static_method(3, 4))

print(MyClass.class_method(5, 1))

