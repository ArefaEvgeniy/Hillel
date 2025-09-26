import time


def get_data():
    def get_cpu(data):
        ...
        return data

    def get_memory(data):
        ...
        return data

    def get_process(data):
        ...
        return data

    data = {}
    data = get_cpu(data)
    data = get_memory(data)
    data = get_process(data)

    return data


def process_data(data):
    new_data = {}
    ...
    return new_data


def print_data(new_data):
    ...


def main():
    while True:
        data = get_data()
        new_data = process_data(data)
        print_data(new_data)

        time.sleep(2)


main()
