import os

import requests

from dotenv import load_dotenv
from downloader import download_img


DIR_IMG_XKCD = 'comics_xkcd'


def download_comics_img(save_dir: str):
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()

    comics_img = response.json()
    url = comics_img['img']

    download_img(url, save_dir)

    print('Comment:', comics_img['alt'])


if __name__ == '__main__':
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    vk_kclient_id = os.environ["VK_CLIENT_ID"]
    print(vk_kclient_id)

    download_comics_img(DIR_IMG_XKCD)
