lst1 = [_ for _ in range(100) if _ % 3 == 0]

import random

a = random.randint(1, 2)
new_list = []
for _ in range(random.randint(1, 100)):
    if a == 1:
        new_list.append(1)
    else:
        new_list.append(0)

lst2 = [1 if a == 1 else 0 for _ in range(100)]



# -----------
hashtag_str = "hello world, this is a hashtag"
hashtag_str = "".join(hashtag_str.title().split())
print(hashtag_str)



# -----------
import keyword

my_string = "_"
# myres = True
# if my_string == "":
#     myres = False

myres = (not my_string[0].isdigit()) & (my_string not in keyword.kwlist)
