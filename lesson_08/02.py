# Наведено список балів 10 студентів на іспиті з хімії.
# Відфільтрувати тих, хто здав із балом вище 75... використовуючи filter().


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75, 99, 12]

print(list(filter(lambda x: x > 75, scores)))
