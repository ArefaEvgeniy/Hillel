score = (66, 50, 75, 100, 99, 12, 77, 12, 86, 56, 78)


def more_75(score):
    return score > 75


print(list(filter(more_75, score)))

print(set(filter(lambda x: x > 75, score)))
