lst = ['a', 'b']
t = (1, 2, 5, lst, 333, 667)
print(t)
lst = ['w', 'z']
# lst[0] = 'w'
# lst[1] = 'z'
print(t)
print(lst in t)
print(['a', 'b'] in t)
