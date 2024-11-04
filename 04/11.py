# Доступ до елементів списку за допомогою циклу while
lst = [4, 6, 8, 7]
i = 0
while i < len(lst):
    l = lst[i]
    print(l ** 2)
    i += 1

print('-' * 100)

# Те ж саме, але за допомогою циклу for
lst = [4, 6, 8, 7]
for item in lst:
    print(item ** 2)
