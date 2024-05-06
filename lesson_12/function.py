import time


def get_data():
    def get_cpu(data):
        ...
        return data

    def get_memory(data):
        ...
        return data

    def get_processors(data):
        ...
        return data

    def get_fun(data):
        ...
        return data

    data = {}
    data = get_cpu(data)
    data = get_memory(data)
    data = get_processors(data)
    data = get_fun(data)
    return data


def prepare_data(data):
    result = ''
    ...
    return result


def print_data(data):
    ...


def main():
    while True:
        data = get_data()
        new_data = prepare_data(data)
        print_data(new_data)
        time.sleep(2)


if __name__ == '__main__':
    main()
