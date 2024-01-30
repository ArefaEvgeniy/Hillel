e = [12, 11, 10]           # 140279013714240 -> [12, 11, 10]
f = e                      # 140279013714240 -> [12, 11, 10]
print('e = ', e)
print('f = ', f)
print('id e = ', id(e))
print('id f = ', id(f))

f.append(9)                # 140279013714240 -> [12, 11, 10, 9]
print('e = ', e)
print('f = ', f)
print('id e = ', id(e))
print('id f = ', id(f))
