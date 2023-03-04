input_list = [1, 2, 3, 'gg', 'j', 'X']
target = 'j'

index = 0
while index < len(input_list):
    if input_list[index] == target:
        break
    index += 1
else:
    index = -1

print('index:', index)
