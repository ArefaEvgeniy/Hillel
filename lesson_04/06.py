res = None
x = 0
d = [1, 2, 3]

if d:
    print('--if--')
    x /= 10
elif x == 0:
    print('--elif 1--')
    x = 2
elif x < 0:
    print('--elif 2--')
    res = True
    x = abs(x)
else:
    print('--else--')
    res = False
    x -= 2

print('x:', x)
print('res:', res)
