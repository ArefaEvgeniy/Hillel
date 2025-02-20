# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
# 1) ніяких символів з набору string.punctuation не повинно бути, у тому
#    числі й пробілів;
# 2) підсумкова довжина hashtag має бути не більше 140 символів.
# 3) кожне слово починається з великої літери.
# 4) якщо довжина фінішного хештегу більше 140 символів - обрізати 
#    підсумковий рядок до 140 символів.
#
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes


import string
import keyword


result = True
name = input("Введіть рядок: ")
if len(name) > 1 and all(char == '_' for char in name):
    result = False
if name[0].isdigit():
    result = False
if any(char.isupper() or char in string.whitespace or 
       char in string.punctuation.replace('_', '') for char in name):
    result = False
if name in keyword.kwlist:
    result = False

print(result)
