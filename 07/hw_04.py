# Напишіть функцію common_elements, яка згенерує два списки елементів з
# генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5. За допомогою
# множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.
#
#
# def common_elements():
# 		pass
#
#
# common_elements() -> {0, 75, 45, 15, 90, 60, 30}


def common_elements():
    multiple_of_3 = [i for i in range(0, 100) if i % 3 == 0]
    multiple_of_5 = [i for i in range(0, 100) if i % 5 == 0]
    return set(multiple_of_3).intersection(set(multiple_of_5))


print(common_elements())
