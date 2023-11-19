a = 8
c = 'Blue'
result = None

if a > 15 and c == 'Blue':
    print('a > 5')
    result = True
elif a > 11:
    print('a > 11')
    result = 11
elif a > 9:
    print('a > 9')
    result = 9
elif not (a > 7):
    print('a > 7')
    result = 7
elif a > 1:
    print('a > 1')
    result = 1
else:
    print('ELSE')
    result = 0

print('result:', result)
