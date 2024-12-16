class MyManager:

    def __enter__(self):
        return 11

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


with open('new_file.txt') as file:
    ...


aa = MyManager()

with aa as fff:
    ...
