table = [
    [[1, 4, 6, 3], [1, 100, 56, 3, 0], [33, 23, 67]],
    [[44, 55, 66], [95, 96, 97, 98], [59, 99, 67]],
    [[11, 45, 77, 88], [55, 77, 99, 88, 101]]
]

target = 66

found = False
for row, record in enumerate(table):
    for column, field in enumerate(record):
        for index, value in enumerate(field):
            if value == target:
                found = True
                break
        if found:
            break
    if found:
        break
if found:
    print(row, column, index)
else:
    print('not found')


class FoundException(Exception):
    pass


try:
    for row, record in enumerate(table):
        for column, field in enumerate(record):
            for index, value in enumerate(field):
                if value == target:
                    raise FoundException
except FoundException:
    print(row, column, index)
else:
    print('not found')
