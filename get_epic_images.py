import requests
from get_files_functions import download_photo
from parse_inputs import parse_quantity
from datetime import datetime
import os
from dotenv import load_dotenv


def get_epic_images(proxy, quantity):
    epic_url_all = 'https://epic.gsfc.nasa.gov/api/natural'
    proxies = {'https': proxy}
    response = requests.get(epic_url_all, proxies=proxies, verify=False)
    response.raise_for_status()
    response_answer = response.json()[:quantity]
    for image in response_answer:
        date = datetime.fromisoformat(image.get('date'))
        date_formatted = date.strftime("%Y/%m/%d")
        name = image.get('image')
        url = f'https://epic.gsfc.nasa.gov/archive/natural/{date_formatted}/png/{name}.png'
        path = 'images/epic'
        filename = f'{name}.png'
        download_photo(url, path, filename)


def main():
    load_dotenv()
    proxy = os.getenv("PROXY_SOCKS5")
    quantity = int(parse_quantity())
    get_epic_images(proxy=proxy, quantity=quantity)


if __name__ == '__main__':
    main()
