# Дан словарь, создать новый словарь при помощи конструкции
# генератор словаря, поменяв местами ключ и значение.
# chess_players = {
#   "Carlsen, Magnus": 1865,
#   "Firouzja, Alireza": 2804,
#   "Ding, Liren": 2799,
#   "Caruana, Fabiano": 1792,
#   "Nepomniachtchi, Ian": 2773
# }
#
# *Дополнительное не обязательное задание:
# - в новый словарь вставлять только те пары ключ-значение, у которых
# значение в изначальном словаре более 2000;
# - значения нового словаря должны состоять не из фамилии и имени разделённых
# запятой, а из фамилии, только первой буквы имени и точки.
#
# Результат должен быть следующим:
# {
#   2804: 'Firouzja A.',
#   2799: 'Ding L.',
#   2773: 'Nepomniachtchi I.'
# }


chess_players = {
  "Carlsen, Magnus": 1865,
  "Firouzja, Alireza": 2804,
  "Ding, Liren": 2799,
  "Caruana, Fabiano": 1792,
  "Nepomniachtchi, Ian": 2773
}

new_chess_players = {value: key for key, value in chess_players.items()}

best_players = {value: f"{key.split()[0].strip(',')} {key.split()[1][0]}."
                for key, value in chess_players.items() if value > 2000}

print(new_chess_players)
print(best_players)
