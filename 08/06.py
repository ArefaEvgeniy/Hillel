def func(a, b, c=99, d=None):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print("------------------")


a = 10
b = 56
c = 0
func(b=c, c=a, a=556)
func(b=c, a=556)
func(777, c=a, b=0)
# func(777, c=a, a=0)
func(0, 777, c=a)
