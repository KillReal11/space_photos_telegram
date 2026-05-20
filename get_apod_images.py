import requests
import os
from dotenv import load_dotenv
from get_files_functions import get_image_name_extension, download_photo
from parse_inputs import parse_quantity


def get_apod_images(nasa_api_key, proxy, quantity):
    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_api_key, 'count': quantity}
    proxies = {'https': proxy}
    response = requests.get(apod_url, params=params, proxies=proxies, verify=False)
    response.raise_for_status()
    response_answer = response.json()
    for image in response_answer:
        image_url = image.get('url')
        path = 'images/apod'
        image_name = get_image_name_extension(image_url)[0]
        download_photo(image_url, path, image_name)


def main():
    load_dotenv()
    proxy = os.getenv("PROXY_SOCKS5")
    nasa_api_key = os.getenv("NASA_API_KEY")
    quantity = parse_quantity()
    get_apod_images(nasa_api_key=nasa_api_key, proxy=proxy, quantity=quantity)


if __name__ == '__main__':
    main()
