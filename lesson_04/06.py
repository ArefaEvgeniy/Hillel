# Ввести предложение.
# Если в предложении есть слово code - вывести на экран Yes, 1
# Если в предложении есть слово codec - вывести на экран Yes, 2
# Иначе вывести на экран No

input_str = input("Enter: ")

if 'codec' in input_str:
    print('Yes, 2')
    if 'xxx' in input_str:
        print('Yes, 3')
    else:
        print('No, No')
elif 'code' in input_str:
    print('Yes, 1')
else:
    print('No')
