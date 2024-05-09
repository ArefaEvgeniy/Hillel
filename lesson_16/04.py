import time


class MyClass:
    start = 0

    def __next__(self):
        self.start += 1
        while self.start <= 500000:
            return self.start
        raise StopIteration

    def __iter__(self):
        return self


my_list = MyClass()

for item in my_list:
    print(item)
    # time.sleep(1)


