# Даний словник
# Створити новий словник, ключами якого буде результат конкатенації ключа
# старого словника та довжини цього ключа, а значенням буде квадрат
# початкового значення, якщо початкове значення типу int, інакше значенням
# буде довжина початкового значення

old_dict = {'aa': 1, 'b': 2, 'ccc': 3, 'ddd': '11'}

new_dict = {f'{key}{len(key)}': value ** 2 if isinstance(value, int) else len(value) for key, value in old_dict.items()}
print(new_dict)
