x = -10

if x >= 0:
    a_1 = True
else:
    a_1 = False

a_2 = True if x >= 0 else False

print(f'a_1: {a_1}')
print(f'a_2: {a_2}')


x = 0

if x > 0:
    b_1 = True
elif x == 0:
    b_1 = None
else:
    b_1 = False

b_2 = True if x > 0 else None if x == 0 else False

print(f'b_1: {b_1}')
print(f'b_2: {b_2}')
