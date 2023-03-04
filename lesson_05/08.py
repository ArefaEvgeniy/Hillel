value_1 = 't'

num_1 = int(value_1) if value_1.isdigit() else 1 if len(value_1) > 1 else 0
print('num_1:', num_1)

if value_1.isdigit():
    num_1 = int(value_1)
else:
    if len(value_1) > 1:
        num_1 = 1
    else:
        num_1 = 0
