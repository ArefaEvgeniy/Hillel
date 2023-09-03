c = int(input())

q = 1
result = 1
while c > q:
    if q == 3:
        q += 1
        continue
    if q == 7:
        break
    result *= q
    q += 1
    print(q)
else:
    print('FINISH')

print('result:', result)
