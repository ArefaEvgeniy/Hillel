def example_function(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("------------------")


my_dict = {'a': 1, 'c': 3, 'b': 2}
example_function(**my_dict)  # example_function(a=1, c=3, b=2)
