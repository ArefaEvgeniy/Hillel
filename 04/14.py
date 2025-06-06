a = ['ertre', '567', '223', 'ee5', '457u', '689', '7788', 'yy7']

result = 0

for item in a:
    if item.isdigit():
        result += int(item)
else:
    print('else')

print('result:', result)

