my_list = [1, 0, 56, ['er', 'tt'], 2]

for item in my_list:
    if isinstance(item, (dict, list, tuple, set)):
        for value in item:
            print('\t', value)
    else:
        print(item)
else:
    print('else')
