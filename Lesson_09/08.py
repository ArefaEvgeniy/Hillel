names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
ages = [25, 30]
phones = ('123-456-7890', '987-654-3210', '555-555-5555')

zipped_data = zip(names, ages, phones)
result = list(zipped_data)

print(result)
