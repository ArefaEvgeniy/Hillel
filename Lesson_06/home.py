name = input("Введіть ім'я змінної: ")
if name in ("_", "x", "get_value", "some_super_puper_value", "m3", "assert_exception"):
    print(True)
else:
    print(False)
