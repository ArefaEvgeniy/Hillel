class MyClass(str):
    def __iter__(self):
        self.value = self.split()
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if self.count < len(self.value):
            return self.value[self.count].title().strip(',').strip('.')
        raise StopIteration


my_str = MyClass('Це УЧБОВЕ завдання на строки, воно допоможе оволодіти ІТЕРАТОРАми.')

a = iter(my_str)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# for item in my_str:
#     print(item)

