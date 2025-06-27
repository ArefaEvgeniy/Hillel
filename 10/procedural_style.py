import time


def get_data():
     def get_data_cpu(data):
         ...

     def get_data_memory(data):
         ...

     def get_data_process(data):
         ...

     data = {}
     data = get_data_cpu(data)
     data = get_data_memory(data)
     data = get_data_process(data)

     return data


def prepare_data(data):
    new_data = []
    ...
    return new_data


def print_data(data):
    ...


def main():
    while True:
        data = get_data()
        prepared_data = prepare_data(data)
        print_data(prepared_data)
        time.sleep(3)


main()
