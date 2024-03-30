# Ввести речення.
# Якщо у реченні є слово code - вивести на екран Yes, 1
# Якщо у реченні є слово codec - вивести на екран Yes, 2
# Інакше вивести на екран No

word = input('Enter your word: ')

if 'code' in word:
    print('Yes, 1')
elif 'codec' in word:
    print('Yes, 2')
else:
    print('No')
