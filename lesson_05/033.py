aa = 'Hello, word'
for index, item in enumerate(aa):
    if not item.isalpha():
        continue
    if item == ' ':
        break
    print(f'{index} - {item}')
else:
    print('ELSE')
