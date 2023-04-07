class FoundNamberException(Exception): pass


table = [[[1, 2, 3, 4], [5, 3, 22, 5]], [[1, 7], [99, 345], [44, 5]], [[8, 7, 6], [101, 102]]]
target = 99

found = False
for row, record in enumerate(table):
    for col, field in enumerate(record):
        for index, item in enumerate(field):
            if item == target:
                found = True
                break
        if found:
            break
    if found:
        break
if found:
    print(f'found {target}, indexes: {row+1}, {col+1}, {index+1}')
else:
    print('not found')


try:
    for row, record in enumerate(table):
        for col, field in enumerate(record):
            for index, item in enumerate(field):
                if item == target:
                    raise FoundNamberException
except FoundNamberException:
    print(f'found {target}, indexes: {row+1}, {col+1}, {index+1}')
else:
    print('not found')
