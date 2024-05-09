class MyIter:
    def __init__(self, input_value):
        self.value = input_value.split()
        self.count = -1

    def __next__(self):
        self.count += 1
        if self.count < len(self.value):
            return self.value[self.count].title().strip(',').strip('.')
        raise StopIteration


class MyClass(str):
    def __iter__(self):
        return MyIter(self)


my_str = MyClass('Це УЧБОВЕ завдання на строки, воно допоможе оволодіти ІТЕРАТОРАми.')

# a = iter(my_str)
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for item in my_str:
    print(item)

