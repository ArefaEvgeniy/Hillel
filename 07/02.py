while True:
    ...
    answer = input("Enter y/Yes/т/Так to work: ").lower()
    # if answer == 'y' or answer == 'yes' or answer == 'т' or answer == 'так':
    if answer in ('y', 'yes', 'т', 'так'):
        break
