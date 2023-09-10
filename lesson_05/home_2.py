# Даний словник, створити новий словник, змінивши місцями ключ та значення.
# У новий словник вставляти лише ті пари ключ-значення, які мають значення
# у початковому словнику понад 2000
# chess_players = {
#   "Carlsen, Magnus": 1865,
#   "Firouzja, Alireza": 2804,
#   "Ding, Liren": 2799,
#   "Caruana, Fabiano": 1792,
#   "Nepomniachtchi, Ian": 2773
# }
#
# *Додаткове не обов'язкове завдання:
# значення нового словника повинні складатися не з прізвища та імені розділених
# комою, а з прізвища, тільки першої літери імені та точки.
# Результат має бути наступним:
# new_chess_players = {
# 2804: 'Firouzja A.',
# 2799: 'Ding L.',
# 2773: 'Nepomniachtchi I.'
# }


chess_players = {
  "Carlsen, Magnus": 2865,
  "Firouzja, Alireza": 1804,
  "Ding, Liren": 2799,
  "Caruana, Fabiano": 2792,
  "Nepomniachtchi, Ian": 1773
}

new_chess_players = {value: key for key, value in chess_players.items()}

best_players = {value: f"{key.split()[0].strip(',')} {key.split()[1][0]}."
                for key, value in chess_players.items() if value > 2000}

print(chess_players)
print(best_players)
