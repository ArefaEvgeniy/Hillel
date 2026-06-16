def func(a, *args, b=66):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    for item in args:
        print(item)
    print("------------------")


a = 10
b = 56
c = 0
func(c, a, 556, b=77)
func(c, a)
# func(c)
func(c, a, 556, "ewter", 767, -100, 0, "dsgdf", [1, 33, {3: "hello"}, 89])
# func()

