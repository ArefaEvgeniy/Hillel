a = -30
b = []

print('START')
while a > 0:
    print('start while')
    if a <= 3:
        break
    if a != 5:
        b.append(a)
    a -= 1
    print('end while')
else:
    print('ELSE')
print('b:', b)
print('END')
