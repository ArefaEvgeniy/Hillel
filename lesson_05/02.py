a1 = []
for i in range(1, 16):
    if i % 4:
        a1.append(i * 2)

print(f'a1: {a1}')


a2 = [i * 2 for i in range(1, 16) if i % 4]
print(f'a2: {a2}')
