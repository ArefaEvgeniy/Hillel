old_dict = {'aa': 1, 'b': 2, 'cccc': 3}

#new_dict = {'aa2': 1, 'b1': 4, 'cccc4': 9}

new_dict = {key + str(len(key)): value ** 2 for key, value in old_dict.items()}

print(new_dict)
