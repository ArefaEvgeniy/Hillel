# class MyClass_2:
#     def __init__(self):
#         self.value = 0
#
#     def __next__(self):
#         self.value += 1
#         if self.value < 10:
#             return self.value
#         raise StopIteration


class MyClass:
    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        if self.value < 10:
            return self.value
        raise StopIteration


a = MyClass()

# for item in a:
#     print(item)

print(a)
b = iter(a)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
b.value = 0

print('-' * 100)

for item in b:
    print(item)
