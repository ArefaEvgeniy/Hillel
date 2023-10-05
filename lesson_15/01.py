print('Start')
y = int(input())


def my_func(y):
    x = None
    try:
        x = 1 / y
    except LookupError:
        print('LookupError 2')
    # except ZeroDivisionError:
    #     print('ZeroDivisionError 2')
    return x


try:
    x = my_func(y)
except LookupError:
    print('LookupError')
except KeyError:
    print('KeyError')
    x = 1
except ZeroDivisionError:
    print('ZeroDivisionError')
    x = 0
except EOFError:
    print('EOFError')
else:
    print('else')
finally:
    print('finally')


print(f'x={x}')
print('END')


f = open('dfd')
...
f.close()

try:
    f = open('dfd')
    ...
finally:
    f.close()
