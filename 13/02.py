def func(a, b):
    print("Start Func")
    try:
        res = ((a + 4) * 5) / b[5]
        print("CONTINUE")
    except ZeroDivisionError:
        print("EXCEPTION ZeroDivisionError")
        res = 0
    except TypeError:
        print("EXCEPTION TypeError")
        res = None

    print("End Func")
    return res


print("START")
try:
    a = 10
    z = func(a, [4, 3])
except IndexError:
    print("EXCEPTION IndexError")
    z = "!!!"

print("z:", z)
print("END")
