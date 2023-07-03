c = int(input("Enter number: "))

q = 0
result = 1
while c > q:
    q += 1
    result *= q

print(f'result: {result}')


result_2 = 1
for item in range(1, c + 1):
    result_2 *= item

print(f'result_2: {result_2}')
