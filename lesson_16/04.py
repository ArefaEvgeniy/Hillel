def my_generator(start=1, step=1, ups_val=1000):
    val = start
    while True:
        yield val
        val *= step
        if abs(val) >= ups_val:
            break


for item in my_generator(-2, -5):
    print(item)
