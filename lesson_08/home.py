# Написать декоратор к 2-м любым функциям, который бы
# считал и выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()


from datetime import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time}")
        return result
    return wrapper


@timer
def function1():
    # Код первой функции
    ...


@timer
def function2():
    # Код второй функции
    ...


# Вызов функций
function1()
function2()
