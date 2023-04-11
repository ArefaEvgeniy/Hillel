#Создать генератор геометрической прогрессии:


def simple_generator(start, step):
    ...


for item in simple_generator(-2, -5):
    print(item)
    if -1000 <= item >= 1000:
        break

# -2
# 10
# -50
# 250
# -1250
# 6250

for item in simple_generator(10, 3):
    print(item)
    if -1000 <= item >= 1000:
        break

# 10
# 30
# 90
# 270
# 810
# 2430
