def bubble_sort(seq):
    for i in range(len(seq) - 1, 0, -1):
        print(seq)
        print('-' * 50)
        no_swap = True
        for j in range(0, i):
            print(seq)
            if seq[j + 1] < seq[j]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                no_swap = False
        if no_swap:
            return


seq = [50, 3, 6, -10, 345, 234, 5, 67, -113, 23, 456, 2, 9, 8, 55]
print('before sort:', seq)

bubble_sort(seq)

print('after sort:', seq)


# [-113, -10, 2, 3, 5, 6, 8, 9, 23, 50, 55, 67, 234, 345, 456]
#
# [-113, -110, -100, -90, -80, -70, -65, -60, -50, -40, -30, -25, -20, 2, 456]
#
# [-113, 2, 3, 4, 5, 6, 8, 9, 23, 50, 55, 67, 234, 345, 456]
#
# [-113, -10, 2, 3, 5, 6, 8]
# [-113, -10, 2]
# [2]
