table = [
    [[1, 4, 6, 3], [1, 100, 56, 3, 0], [33, 23, 67]],
    [[44, 55, 66], [95, 96, 97, 98], [59, 99, 67]],
    [[11, 45, 77, 88], [55, 77, 99, 88, 101]]
]

target = 101

found = False
for row, record in enumerate(table):
    for column, field in enumerate(record):
        for index, item in enumerate(field):
            if item == target:
                found = True
                break
        if found:
            break
    if found:
        break
if found:
    print("found at ({0}, {1}, {2})".format(row+1, column+1, index+1))
else:
    print("not found")


class MyException(Exception):
    pass


try:
    for row, record in enumerate(table):
        for column, field in enumerate(record):
            for index, item in enumerate(field):
                if item == target:
                    raise MyException
except MyException:
    print("found at ({0}, {1}, {2})".format(row+1, column+1, index+1))
else:
    print("not found")
