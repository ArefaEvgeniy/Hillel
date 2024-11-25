def a():
    print('Hello world')


a()
print(a)

b = a

b()

del a

b()
