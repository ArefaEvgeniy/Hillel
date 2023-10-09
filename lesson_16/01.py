sum = 0
for item in [1, 2, 4, 7, 9]:
    sum += item
else:
    print('OK')

print(sum)

sum_2 = 0
i = iter([1, 2, 4, 7, 9])
while True:
    try:
        sum_2 += next(i)
    except StopIteration:
        break
print(sum_2)
