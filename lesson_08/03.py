# Приведен список баллов 10 студентов на экзамене по химии.
# Отфильтровать тех, кто сдал с баллом выше 75 ... используя filter().

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75, 99, 12]


def is_a(score):
    return score > 75


over_75 = list(filter(is_a, scores))
print('over_75:', over_75)

less_70 = list(filter(lambda x: x < 70, scores))
print('less_70:', less_70)
