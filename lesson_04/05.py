x = 16

y = None
if x >= 0:
    print('x more than zero')
    y = True
    if x > 20:
        print('x more than 20')
    if x > 15:
        print('x more than 15')
    if x > 10:
        print('x more than 10')
    else:
        print('x less than 10')
else:
    print('x less than zero')
    y = False
print('ALWAYS')
print('y:', y)
