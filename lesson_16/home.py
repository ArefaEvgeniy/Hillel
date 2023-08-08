# Создать генератор геометрической прогрессии.
# При задании начала прогрессии -2 и шага прогрессии -5,
# генератор выдаёт такую последоваетльность:
# -2
# 10
# -50
# 250
# -1250
# 6250
# ...

# При задании же начала прогрессии 10 и шага прогрессии 3,
# генератор выдаёт такую последоваетльность:
# 10
# 30
# 90
# 270
# 810
# 2430
# ...


def simple_generator(start, step):
    val = start
    while True:
        yield val
        val *= step


for item in simple_generator(-2, -5):
    print(item)
    if -1000 <= item >= 1000:
        break

for item in simple_generator(10, 3):
    print(item)
    if -1000 <= item >= 1000:
        break
