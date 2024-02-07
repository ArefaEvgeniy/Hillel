# Factorial

value = int(input())

result = 1
q = 1
while q <= value:
    result *= q
    q += 1

print(f'result: {result}')


result2 = 1
for item in range(1, value + 1):
    result2 *= item

print(f'result2: {result2}')
