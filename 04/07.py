n = int(input("Enter a number: "))
result = 0

while n > 0:
    if n % 3 == 0:
        n -= 1
        continue
    elif result > 1000:
        break
    result += n
    n -= 1
else:
    print("Factorial calculation is complete.")

print(result)
print(n)
