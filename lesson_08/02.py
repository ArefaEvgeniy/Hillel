# Наведено список балів 10 студентів на іспиті з хімії. Відфільтрувати тих,
# хто здав із балом вище 75... використовуючи filter().

scores = [66, 34, 78, 99, 2, 14, 75, 33, 81, 55]

over_75 = list(filter(lambda x: x > 75, scores))
print(over_75)


def over_50(score):
    return score > 50


print(list(filter(over_50, scores)))
