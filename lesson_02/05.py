s = {1, 2, 3, 4, 5}
s_2 = {1}

print(type(s))
print(len(s) == len(s_2))
print(1 in s)

a = [1, 2, 45, 3, 1, 1, 3, 2, 1, 1, 3, 45, 6, 3]
b = list(set(a))
print(b)
print(set(a))
print(type(b))
