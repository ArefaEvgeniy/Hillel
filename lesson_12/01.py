def read_data():
    ...


def check_data(data):
    result = True
    ...
    return result


def get_alarm(data):
    ...


def process(data):
    new_data = None
    ...
    return new_data


def set_data(data):
    ...


def main():
    data = read_data()
    if not check_data(data):
        get_alarm(data)
    new_data = process(data)
    set_data(new_data)


main()
