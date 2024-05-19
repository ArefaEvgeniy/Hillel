# Створити генератор геометричної прогресії.
# При заданні початку прогресії -2 та кроку прогресії -5,
# генератор видає таку послідовність:
# -2
# 10
# -50
# 250
# -1250
# 6250
# ...
# При заданні початку прогресії 10 і кроку прогресії 3,
# генератор видає таку послідовність:
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

print('-' * 100)

for item in simple_generator(10, 3):
    print(item)
    if -1000 <= item >= 1000:
        break
