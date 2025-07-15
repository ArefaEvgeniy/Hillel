class MyStr(str):

    def __iter__(self):
        self.index = -1
        self.value = self.split()
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.value):
            return self.value[self.index].strip('.,').title()
        raise StopIteration


my_str = MyStr("New StRing методів АбО, як ЩЕ кажуть, реалізувати.")
old_str = "New StRing методів АбО, як ЩЕ кажуть, реалізувати."

iter(my_str)
print(next(my_str))
print(next(my_str))
print('-' * 100)

for item in my_str:
    print(item)

iter(my_str)
print(next(my_str))
