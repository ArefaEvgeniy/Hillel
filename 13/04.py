try:
    a = 10
    b = [0, 5]
    print('start')

    c = a / b
    print('more')
except ZeroDivisionError:
    c = 0
else:
    print('ELSE')
finally:
    print('finally')


print(c)

print('end')
