# Написати декоратор до 2-х будь-яких функцій, який би вважав та виводив
# час їх виконання.
# Підсказка:
# from datetime import datetime
# now = datetime.now()

from datetime import datetime
import time


def dec_time_measure(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        res = func(*args, **kwargs)
        print(f"Время выполнение функции {func.__name__}: {datetime.now() - now} секунд")
        return res

    return wrapper


@dec_time_measure
def testFunc1():
    print("Выполняется функция testFunc1")
    time.sleep(1)
    print("Функция testFunc1 выполнена")


@dec_time_measure
def testFunc2():
    print("Выполняется функция testFunc2")
    time.sleep(2)
    print("Функция testFunc2 выполнена")


testFunc1()
testFunc2()
