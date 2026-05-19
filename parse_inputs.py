import argparse
from get_files_functions import get_random_file


def parse_id():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'spacex_id',
        default='latest',
        nargs='?',
        help='Введите id запуска spacex. По умолчанию: latest'
        )
    args = parser.parse_args()
    return args.spacex_id


def parse_quantity():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'quantity',
        default='30',
        nargs='?',
        help='Введите количество фотографий, которое хотите скачать. По умолчанию: 30'
        )
    args = parser.parse_args()
    return args.quantity


def parse_path():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path',
        default=get_random_file(),
        nargs='?',
        help='Введите путь фото. По умолчанию публикуется случайное фото'
        )
    args = parser.parse_args()
    return args.path
