import argparse
from get_files_functions import get_random_file


def parse_id():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'spacex_id',
        default='latest',
        nargs='?',
        help='Введите id запуска spacex.\n'
        'Пример id: 5eb87d47ffd86e000604b38a.\n'
        'По умолчанию: %(default)s'
        )
    args = parser.parse_args()
    return args.spacex_id


def parse_quantity():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'quantity',
        default='30',
        nargs='?',
        help='Введите количество фотографий, которое хотите скачать.\n'
        'Например: 12.\n'
        'По умолчанию: %(default)s'
        )
    args = parser.parse_args()
    return args.quantity


def parse_path():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'path',
        default=get_random_file(),
        nargs='?',
        help='Введите путь к фото. \n'
        'Например: %(default)s.\n'
        'По умолчанию публикуется случайное фото из папки images.'
        )
    args = parser.parse_args()
    return args.path
