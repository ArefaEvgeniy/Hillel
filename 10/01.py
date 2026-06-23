import time


def my_decorator(func):
    def wrapper():
        start = time.time()
        func()
        print(f"Execution time: {time.time() - start} seconds")
    return wrapper
