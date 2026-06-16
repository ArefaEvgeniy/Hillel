def example_function(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("------------------")


my_list = (1, 2, 3)
example_function(56, 76, 0)
example_function(my_list[0], my_list[1], my_list[2])
example_function(*my_list)  # example_function(1, 2, 3)
