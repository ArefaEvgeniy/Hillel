a = 0

if a > 0:
    c = True
elif a == 0:
    c = None
else:
    c = False

print(c)

d = True if a > 0 else False
d = True if a > 0 else (None if a == 0 else False)
print(d)

print(True) if a > 0 else print(False)
