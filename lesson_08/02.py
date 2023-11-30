# Наведено список балів 10 студентів на іспиті з хімії. Відфільтрувати тих,
# хто здав із балом вище 75... використовуючи filter().

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75, 99, 12]


def is_A_student(score):
    return score > 75


over_75_1 = list(filter(is_A_student, scores))
over_75_2 = list(filter(lambda x: x > 75, scores))

print(over_75_1)
print(over_75_2)
