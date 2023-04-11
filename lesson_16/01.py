values = [1, 2, 4, 8]

res = 1
for item in values:
    res *= item
print('result:', res)

res_2 = 1
iterator = iter(values)
while True:
    try:
        res_2 *= next(iterator)
    except StopIteration:
        break
print('result_2:', res_2)
