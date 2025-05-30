a = 101
c = True
d = 0

if a > 100:
    print('a > 100')
    a -= 35
    c = True
if a < 0:
    print('a < 0')
    a = abs(a)
# if ((a >= 0 and a <= 100 and c is True) or (a < 0 and c is False)) or d == 1000:
if 0 <= a <= 100:
    print('0 <= a <= 100')

print("a:", a)
print('END')
