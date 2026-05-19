import requests
from pathlib import Path
from urllib.parse import urlsplit
from urllib.parse import unquote
import os
import random


def get_image_name_extension(image_url):
    image_url_splitted = urlsplit(image_url)
    image_extension = os.path.splitext(image_url_splitted.path)[1]
    image_name_raw = os.path.split(image_url_splitted.path)[-1]
    image_name = unquote(image_name_raw, encoding='utf-8', errors='replace')
    return image_name, image_extension


def download_photo(url, path, filename):
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f'{Path(path)}/{filename}', 'wb') as file:
        file.write(response.content)


def get_random_file():
    all_files = []
    for root, dirs, files in os.walk('images'):
        for file in files:
            all_files.append(os.path.join(root, file))
    random_file = random.choice(all_files)
    return random_file
