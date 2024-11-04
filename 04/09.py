# Варіант обходу списку списків за допомогою циклу while
first_list = [[1, 2, 3], [4, 5, 6]]
i = 0
while i < len(first_list):
    j = 0
    lst = first_list[i]
    while j < len(lst):
        print(lst[j])
        j += 1
    i += 1

print('-' * 100)

# Варіант обходу списку списків за допомогою циклу for
first_list = [[1, 2, 3], [4, 5, 6]]
for lst in first_list:
    for j in lst:
        print(j)
