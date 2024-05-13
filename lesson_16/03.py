class MyClass:
    def __init__(self, value=None):
        if value is None:
            value = []
        self.value = list(value)
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count >= len(self.value):
            self.count = 0
        return self.value[self.count]
        # raise StopIteration


my_list = MyClass(['1', '45', 77, 0, True, 'sdgdfg', 100])

# __iter__() -> повертає ітератор на об'єкт - ітеріруємий об'єкт
# __next__() -> повертає наступний елемент ітеріруємого об'єкта - об'єкт ітератор
# StopIteration

for item in my_list:
    print(item)

