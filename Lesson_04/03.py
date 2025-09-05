number = 30
result = 1

while number > 1:
    if number % 3 == 0:
        number -= 1
        continue
    result *= number
    if result > 100000:
        result /= number
        result = int(result)
        break
    number -= 1
else:
    print('ELSE')

print('result:', result)

