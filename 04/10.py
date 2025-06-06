a = 999

result = 1
i = 1

while i <= a:
    if i % 3 == 0:
        i += 1
        print('continue')
        continue
    if i % 1000 == 0:
        print('break')
        break
    result *= i
    i += 1
else:
    print('End WHILE')

print('result:', result)

