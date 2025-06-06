a = ['ertre', '567', '223', 'ee5', '457u', '689', '7788', 'yy7']

result = 0
index = 0
index_list = []

for item in a:
    if item.isdigit():
        result += int(item)
        index_list.append(index)
    index += 1

print('result:', result)
print('index_list:', index_list)
