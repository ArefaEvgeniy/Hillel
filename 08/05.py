def func(b, a=1, c=99, d=None):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print("------------------")


a = 10
b = 56
c = 0
func(c, a, b)
func(c, a)
func(c, a, {3: "hello", "world": 89})
func(100)
