# Написать программу аналог команды top или htop для Linux-систем.
# Программу написать на основе данных полученных из утилиты psutil.
# Вывод необходимо сделать по возможности красивым и максимально
# приближенным к выводу команд top или htop.
# В начале необходимо в графическом виде и виде процентов вывести информацию
# о частоте и загрузке процессоре, а атк же о памяти: используемая/доступная.
# После этого необходимо в табличном виде вывести информацию о первых 30 -
# 35 процессах разбитой по столбцам: pid, username, cpu, memory, time, command.
# В каждой новой строке информация о новом процессе, на подобии как в top.
# Желательно, чтобы как по аналогии с командами top или htop информация
# постоянно обновлялась, где-то через каждые 2-3 секунды.
# Предусмотреть возможность сортировки процессов по любому из параметров.
# Как вариант, это можно сделать при помощи аргументов при запуске скрипта (argparse).
# Ссылка как вывод сделать цветным: https://egorovegor.ru/python-color-printing/

import argparse
import psutil
import time


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', metavar='--sort', type=str, help='Name of item for sort')
    parser.add_argument('-r', metavar='--reverse', type=str, help='Reversed sort')

    return parser.parse_args()


def get_processes():
    result = []
    return result


def get_cpu():
    freq = percent = None
    return freq, percent


def get_memory():
    total = used = percent = None
    return total, used, percent


def print_info(pids, cpu, memory):
    print('cpu...')
    print('memory...')
    for index, item in enumerate(pids):
        if index > 35:
            break
        print('...')


def main():
    parser = create_parser()

    while True:
        pids = get_processes()
        cpu = get_cpu()
        memory = get_memory()
        print_info(pids, cpu, memory)


if __name__ == '__main__':
    main()
