x = -10
a = input()

print('Start')
if a:
    print('IF')
    print('x > 0')
    if x < -1:
        print('x < -1')
    print('ENDIF')
    ...
elif x == 0:
    print('x == 0')
elif x < -5:
    print('x < -5')
elif x < -7:
    pass
else:
    print('ELSE')

print('Finish')
