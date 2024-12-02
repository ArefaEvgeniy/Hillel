import time


def get_data():
    def get_CPU():
        pass

    def get_memory():
        pass

    def get_processes():
        pass

    data = []
    data.append(get_CPU())
    data.append(get_memory())
    data.append(get_processes())
    return data


def prepare_data(data):
    new_data = None
    ...
    return new_data


def print_data(data):
    ...


def main():
    while True:
        data = get_data()
        new_data = prepare_data(data)
        print_data(new_data)
        time.sleep(2)


main()
