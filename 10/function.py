import time


def get_data():
    def get_cpu():
        data = ""
        ...
        return data

    def get_memory():
        data = ""
        ...
        return data

    def get_processes():
        data = []
        ...
        return data

    def get_temperature():
        data = ""
        ...
        return data

    data = {
        "cpu": get_cpu(),
        "memory": get_memory(),
        "processes": get_processes(),
        "temperature": get_temperature()
    }
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
        new_data = prepare_data(data)
        print_data(new_data)
        time.sleep(2)


main()
