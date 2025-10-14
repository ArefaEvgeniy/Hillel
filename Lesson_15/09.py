# f = open("Lesson_15/09.py", "r")
# content = f.read()
# print(content)
# f.close()
#
#
# with open("Lesson_15/09.py", "r") as f:
#     content = f.read()
#     print(content)


class MyContextManager:
    def __enter__(self):
        print("Entering the context...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context...")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exception if any


my_data = MyContextManager()

with my_data as data:
    print("Start with")
    print("End with")
