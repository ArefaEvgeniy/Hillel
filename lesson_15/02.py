def func(a, b):
    print('Before')
    c = int(a) / int(b)
    print('After')
    return c


try:
    a = input()
    b = input()
    res = func(a, b)
    print(f'Result: {res}')
except Exception:
    print('Exception')
