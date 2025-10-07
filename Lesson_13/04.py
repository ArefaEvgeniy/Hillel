def func(a, b, d):
    try:
        print("Before exception")
        c = a / b  # ZeroDivisionError: division by zero
        e = d[2]
        print(e)
        print("After exception")
    # except (ZeroDivisionError, IndexError):
    except ZeroDivisionError:
        print("Division by zero")
        c = 0
        e = 0

    print("end of func")
    ...

    return c, e


print("START")
a = 10
b = 4
d = [1, 2, 3]

try:
    z, x = func(a, b, d)
except IndexError:
    print("Index error in main")
    z = None
    x = None

print(z)
print(x)
print("END")
