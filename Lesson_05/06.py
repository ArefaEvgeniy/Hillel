a = '   Enter a number from 0 to 100:    '

list_of_worlds = a.split('er ')
print(list_of_worlds)
print(a.strip(' :0E'))

print("---".join(list_of_worlds))

list_of_names = ['Bob', 'Alice', 'John', 'Ann']

print('My friends are: ' + ', '.join(list_of_names) if list_of_names else 'nobody' + '.')
