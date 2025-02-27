# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок
# паліндромом. Паліндромом - це такий рядок, який читається однаково зліва
# направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
#
# def is_palindrome(text):
#     pass
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

def check(my_variable):
    filtered_text = "".join(char.lower() for char in my_variable if char.isalnum())
    return filtered_text == filtered_text[::-1]


print(check('A man, a plan, a canal: Panama'))
print(check('0P'))
print(check('a.'))
print(check('aurora'))
print(check('Топ.пОт '))
