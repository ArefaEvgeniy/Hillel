a = 100
print("sfnsfkl", sep='---')
print(a)
print()
# print("a is :", a, "and type of a is", type(a), sep='---')
print("a is :", a, "and type of a is", sep='---', end=' ')
print(type(a))

with open("file.txt", "w") as my_file:
    print("Maksim", file=my_file)

a = 46700
n = len(str(a))
print(n)
