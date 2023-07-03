# Дан список словарей.
# Каждый словарь описывает машину(серийный номер и год выпуска).
# Создать новый список со всеми машинами, год выпуска которых больше 2006.

BASE_CAR = [
    {'number': 'AE12232', 'year': 2020},
    {'number': 'AE11111', 'year': 2010},
    {'number': 'AE33333', 'year': 2022},
    {'number': 'BC88974', 'year': 1999},
    {'number': 'AE55555', 'year': 2001},
    {'number': 'AE15552', 'year': 2006}
]

new_list = [{i['number']: i['year']} for i in BASE_CAR if i['year'] > 2006]

print(new_list)
