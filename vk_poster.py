import os

import requests

from dotenv import load_dotenv
from downloader import download_img


DIR_IMG_XKCD = 'comics_xkcd'


def download_comics_img(save_dir: str) -> dict:
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()

    comics_img = response.json()
    url = comics_img['img']

    img_path = download_img(url, save_dir)
    img_comment = comics_img['alt']

    return {'path': img_path, 'comment': img_comment}


def get_upload_url(token: str, group_id: str, version_api: str) -> str:
    payload = {'access_token': token, 'group_id': group_id, 'v': version_api}
    url = 'https://api.vk.com/method/photos.getWallUploadServer'

    response = requests.get(url, params=payload)
    response.raise_for_status()

    upload_url = response.json()['response']['upload_url']

    return upload_url


if __name__ == '__main__':
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    client_id = os.environ['VK_CLIENT_ID']
    group_id = os.environ['VK_GROUP_ID']
    token = os.environ['VK_TOKEN']
    version_api = os.environ['VK_V_API']

    img_data = download_comics_img(DIR_IMG_XKCD)
    upload_url = get_upload_url(token, group_id, version_api)
