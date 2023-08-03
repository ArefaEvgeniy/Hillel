# __iter__()

# __next__()
# raise StopIteration

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

print('-' * 50)

# i = my_list.__iter__()
i = iter(my_list)
print(i)
while True:
    try:
        # print(i.__next__())
        print(next(i))
    except StopIteration:
        break
