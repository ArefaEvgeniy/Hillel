a = ['ertre', '567', '223', 'ee5', '457u', '689', '7788', 'yy7']

result = 0
index_list = []

for index, item in enumerate(a):
    if item.isdigit():
        result += int(item)
        index_list.append(index)

print('result:', result)
print('index_list:', index_list)
print('index:', index)
print('item:', item)
