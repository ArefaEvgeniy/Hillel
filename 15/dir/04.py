class MyList(list):
    def __add__(self, other):
        res = MyList(self)
        for item in other:
            if item not in res:
                res.append(item)
        return res

    def __sub__(self, other):
        res = MyList(self)
        for item in other:
            if item in res:
                res.remove(item)
        return res


list_1 = MyList([1, 6, 3, 4, 5])
list_2 = MyList([0, 4, 2, 1, 7])

list_3 = list_1 + list_2
print(list_3)
list_4 = list_3 - [4, 5]
print(list_4)
