a = 1
b = 2.5
c = "2"
print(a + b)
print(type(a))
print(type(b))
print(type(a + b))

a_1 = str(a)  # "1"
c_1 = int(c)
print(a + c_1)
print(a_1 + c)

print(list(str(float(int((a_1 + c)) + a))))  # "12" -> 12 + 1 -> 13 -> 13.0 -> "13.0"

print(float("34.9".replace(',', '.')))
print(float("34,9".replace(',', '.')))

print(list(str(list((55,)))))  # (55) -> [55] -> "[55]" -> ['[', '5', '5', ']']

print(int(True))
print(tuple(str(float(False))))

print(bool({}))
print(bool({1, 2, 3}))
