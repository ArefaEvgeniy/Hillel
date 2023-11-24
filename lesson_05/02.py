c = int(input('Enter your number: '))

q = 0
result = 1
while c > q:
    q += 1
    result *= q

print('result:', result)


my_list = [1, 3, 4, 'tty', 'frd', 6, 99]
target = 'ttyc'

index = 0
while index < len(my_list):
    if my_list[index] == target:
        break
    index += 1
else:
    index = -1

print('index:', index)
