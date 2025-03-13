try:
    a = 100
    b = 0
    d = [1, 2, 3]
    print('process')
    # c = a + d[10]
    print('second except')
    c = a + '55'
    c = a / b
    print('continue')
except IndexError:
    print('INDEX')
    c = 0
except LookupError:
    print('LookupError')
    c = 100
except (ZeroDivisionError, TypeError) as err:
    c = None
    print(err)
except TypeError:
    c = ""
except Exception as err:
    print('Exception')
    c = 1
    print(err)
else:
    print('OK')
finally:
    print('FINALLY')

print(f"c: {c}")
print('END')
...


# try:
#     a = open('test.txt')
#     ...
# finally:
#     a.close()
