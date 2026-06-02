# 5! = 1 * 2 * 3 * 4 * 5
# 10! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10


n = int(input("Enter a number: "))
result = 1

while n > 1:
    result *= n
    n -= 1
else:
    print("Factorial calculation is complete.")

print(result)
