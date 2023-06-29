x = -5
a = 0

if x > 10:
    print('x > 10')
    a = 10
elif x > 5:
    print('x > 5')
    a = 5
elif x > 0:
    print('x > 0')
    a = True
elif x <= -10:
    print('x is negative')
    a = -10
else:
    print('x is not positive')
    a = False

print(f'a: {a}')


# True and True = True
# True and False = False
# False and True = False
# False and False = False
# True or True = True
# True or False = True
# False or True = True
# False or False = False
#
# not True = False
# not False = True

a = -5
x = 10

if (a > 0 and x > 0 and a < 10) or x < 20:
    print('YES')
else:
    print('NO')


if []:
    print('YES')
else:
    print('NO')
