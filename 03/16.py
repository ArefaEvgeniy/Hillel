a_1 = [34, 67.334, True, ['a', 'b', 34], 'Hello', 455, 0, -100, 200]

print(a_1[3][-1])

a_2 = a_1[0:5]
# a_2 = a_1[:5]
print(a_2)

a_3 = a_1[3:]
print(a_3)

a_4 = a_1[0::2]
print(a_4)

a_4 = a_1[1:-1:3]
print(a_4)

a_5 = a_1[1::3]
print(a_5)

a_6 = a_1[-1:0:-2]
print(a_6)

a_7 = a_1[-1::-2]
print(a_7)

a_8 = a_1[-1::-1]
print(a_8)

a_9 = a_1[::-1]
print(a_9)
