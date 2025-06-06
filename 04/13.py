a = ['ertre', '567', '223', 'ee5', '457u', '689', '7788', 'yy7']

index = 0
result = 0

while index < len(a):
    if a[index].isdigit():
        result += int(a[index])
    index += 1


print('result:', result)

