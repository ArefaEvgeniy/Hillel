def simple_generator(val):
    while val > 0:
        yield 1
        val -= 1


gen_iter = simple_generator(3)
for item in gen_iter:
    print(item)
