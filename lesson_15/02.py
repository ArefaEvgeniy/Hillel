class MyException(Exception): pass


d = {1: 10, 2: 20, 3: 30}

try:
    a = 10 - d[2]
    if a < 0:
        raise MyException
except TypeError:
    print('TypeError')
except IndexError:
    print('IndexError')
except KeyError:
    print('KeyError')
except LookupError:
    print('LookupError')
except MyException:
    print('MyException')
except Exception:
    print('Exception')
