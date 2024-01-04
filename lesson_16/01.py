product = 1
for item in [1, 2, 3, 4, 5]:
    product *= item
print(product)

# iter() -> __iter__()
# next -> __next__()

product_2 = 1
i = iter([1, 2, 3, 4, 5])
# print(i)
# print(type(i))
while True:
    try:
        product_2 *= next(i)
    except StopIteration:
        break
print(product_2)
