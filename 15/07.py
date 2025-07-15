class Counter:

    def __init__(self, string: str):
        self.index = -1
        self.value = string.split()

    def __next__(self):
        self.index += 1
        if self.index < len(self.value):
            return self.value[self.index].strip('.,').title()
        raise StopIteration


class MyStr(str):

    def __iter__(self):
        return Counter(self)


my_str = MyStr("New StRing методів АбО, як ЩЕ кажуть, реалізувати.")
old_str = "New StRing методів АбО, як ЩЕ кажуть, реалізувати."

for item in my_str:
    print(item)


a = iter(my_str)
print(a)
print(type(a))
