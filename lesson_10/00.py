def func(e, r, t):
    ...


a = 99
func(12, t=34, r=a)


def func_2(*args, **kwargs):
    a, b, *c = args
    print(a)
    print(b)
    print(c)


func_2(12, 13, 14, 46, 66, 78)


# ASCII   -   0-127   -   1 Byte
#
# Unicode -               4 Byte  32-bits
#
# UTF-8
# UTF-16
# UTF-32
#
# 00000000    -   0       -   0x00
# 11111111    -   256     -   0xFF
#
# A   -   0x41
# a
# B   -   0x42
#
# 0   -   0
# 1   -   1
# 10  -   2
# 11  -   3
# 100 -   4
# 101 -   5
# 110 -   6
# 111 -   7