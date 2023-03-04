input_number = int(input())

q = 1
result = 1
while input_number >= q:
    result *= q
    q += 1

print('result_1:', result)


result = 1
for item in range(1, input_number+1):
    result *= item
print('result_2:', result)
