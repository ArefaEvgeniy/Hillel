def func(b, a):
    z = 0
    try:
        c = a[1] / b
        z = 1
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        c = 1000

    print(c)
    return z


a = 0
try:
    result = func(a, [])
except Exception as err:
    print(f"Error: {err}")
    result = -1

print(result)
