x = 10
d = {'a': 4, 'b': 12}

try:
    x - d['c']
except (KeyError, LookupError):
    x = 0
except TypeError:
    x = None
except Exception as err:
    print(err)

print(x)
