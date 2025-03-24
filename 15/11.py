class MyIter:
    def __init__(self, start, step, stop=100):
        self.start = start - step
        self.step = step
        self.stop = stop

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        raise StopIteration


obj = MyIter(10, 4, 45)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
