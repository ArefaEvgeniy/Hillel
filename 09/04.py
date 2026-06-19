def fuctorial(n):
    if n <= 1:
        return 1
    else:
        return n * fuctorial(n - 1)


print(fuctorial(4))


n = 4
result = 1
for i in range(1, n + 1):
    result *= i

print(result)
