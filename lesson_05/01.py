number = int(input('Enter your number: '))

count = 0
result = 1
while number > count:
    count += 1
    if count % 5 == 0 and count != 0:
        continue
    result *= count


print('result:', result)
