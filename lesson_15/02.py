a = 12
b = 33
c = 1
d = {1: 'a', 2: 'b'}

try:
    print('START')
    print((a + b) / c)
    print('CONTINUE')
    r = d['1']
    print('CONTINUE 2')
except TypeError:
    if ((type(a) == str and a.isdigit() and type(b) == int) or
            (type(a) == int and type(b) == str and b.isdigit())):
        print(int(a) + int(b))
    else:
        print(str(a) + str(b))
except ZeroDivisionError:
    print('Не можна ділити на нуль')
except KeyError:
    print('Такого ключа не мaє 1')
except LookupError:
    print('Такого ключа не мaє 2')
except Exception:
    print('Щось вішло не так')
else:
    print('ELSE')
finally:
    print('FINALLY')

print('END')
