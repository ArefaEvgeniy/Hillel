# Даний словник
# Створити новий словник, ключами якого буде результат конкатенації ключа
# старого словника та довжини цього ключа, а значенням буде квадрат
# початкового значення, якщо початкове значення типу int, інакше значенням
# буде довжина початкового значення

old_dict = {'aa': 1, 'b': 2, 'cccc': 3, 'ddd': 'red'}
new_dict = {'aa2': 1, 'b1': 4, 'cccc4': 9, 'ddd3': 3}

new_dict2 = {str(key) + str(len(key)): (old_dict[key] ** 2 if type(old_dict[key]) == int else len(old_dict[key])) for key in old_dict}
new_dict3 = {str(key) + str(len(key)): (value ** 2 if isinstance(value, int) else len(value)) for key, value in old_dict.items()}
print(new_dict2)
print(new_dict3)

