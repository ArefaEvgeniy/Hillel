# Наведено список словників.
# Кожен словник описує машину (серійний номер та рік випуску).
# Створити новий список з усіма машинами, рік випуску яких більше n.

BASE_CAR = [
    {'number': 'AE1545BB', 'year': 2020},
    {'number': 'AC5555AA', 'year': 2010},
    {'number': 'EC6674HE', 'year': 2017},
    {'number': 'BA5673OO', 'year': 2022},
    {'number': 'KA345-73', 'year': 2000},
    {'number': 'CA576-28', 'year': 1993}
]

new_car = [i['number'] for i in BASE_CAR if i['year'] > 2000]
print(new_car)
