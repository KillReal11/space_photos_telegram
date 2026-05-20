import requests
from get_files_functions import download_photo
from parse_inputs import parse_id
from dotenv import load_dotenv
import os


def fetch_spacex_last_launch(proxy, spacex_id):
    proxies = {'https': proxy}
    spacex_url = f'https://api.spacexdata.com/v5/launches/{spacex_id}'
    path = 'images/spacex'
    response = requests.get(spacex_url, proxies=proxies, verify=False)
    response.raise_for_status()
    response_answer = response.json()
    images = response_answer.get('links').get('flickr').get('original')
    for number, image in enumerate(images):
        filename = f'spacex{number}.jpg'
        download_photo(image, path, filename)


def main():
    load_dotenv()
    proxy = os.getenv("PROXY_SOCKS5")
    spacex_id = parse_id()
    fetch_spacex_last_launch(proxy=proxy, spacex_id=spacex_id)


if __name__ == '__main__':
    main()
