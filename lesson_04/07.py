# Ввести речення.
# Якщо у реченні є слово code - вивести на екран Yes, 1
# Якщо у реченні є слово codec - вивести на екран Yes, 2
# Інакше вивести на екран No

inputstr = input()

if 'codec' in inputstr:
    print('Yes, 2')
elif 'code' in inputstr:
    print('Yes, 1')
else:
    print('No')
