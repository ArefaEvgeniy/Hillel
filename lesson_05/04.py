a = ['serwe', 'YSF', 'sdfsRTRThjg', 'y', 'TYSFDGH87', 'mjklkwj']

a2 = []
for item in a:
    print('start for')
    if len(item) == 1:
        continue
    if str(item) == 'TYSFDGH':
        break
    a2.append(item.title())
    print('end for')
else:
    print('ELSE')

print(f'a2: {a2}')
