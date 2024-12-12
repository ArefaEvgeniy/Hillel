class My_obj:
    def __init__(self, start, step, stop=33):
        self.start = start
        self.step = step
        self.stop = stop
        self.current = start - step

    def __next__(self):
        self.current += self.step
        if self.current <= self.stop:
            return self.current
        raise StopIteration()

    # def __iter__(self):
    #     return self


class My_obj_2:
    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        return self.iterator


a = My_obj(12, 3)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
b = My_obj_2(a)

for item in b:
    print(item)
