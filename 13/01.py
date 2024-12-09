# a = 10
# b = 0
# if b == 0:
#     c = 0
# else:
#     c = a / b
# print(c)


a = 10
b = 2
print('start')
try:
    c = a / b
    print('more')
except (IndexError, ValueError, ZeroDivisionError, SyntaxError):
    c = 0
print(c)
print('end')
