lst = [1, 2, 3, 4, 5]
print("List_1: ", lst)
if len(lst) >= 2:
    element = lst.pop()
    lst.insert(0, element)
    print("List_2: ", lst)
else:
    print("List_2: ", lst)


lst = [1, 2, 3, 4, 5]
print("List_1: ", lst)
if len(lst) >= 2:
    lst.insert(0, lst.pop())
print("List_2: ", lst)
