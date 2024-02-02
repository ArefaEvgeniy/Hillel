a = -50
d = 0

print('START')
if a > 0:
    print('a is a positive')
    d = 1
    print('end IF')
elif a > -10:
    print('a > -10')
    d = -10
elif a > -20:
    print('a > -20')
    d = -20
elif a > -30:
    print('a > -30')
    d = -30
else:
    print('ELSE')
    d = -1
print('END')
print('d:', d)
