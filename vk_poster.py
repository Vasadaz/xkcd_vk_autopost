import os
import random

import requests

from dotenv import load_dotenv
from downloader import download_img


DIR_IMG_XKCD = 'comics_xkcd'


def download_comics_img(save_dir: str) -> dict:
    comics_random_num = random.randint(0, get_last_comic())
    response = requests.get(f'https://xkcd.com/{comics_random_num}/info.0.json')
    response.raise_for_status()

    comics_img = response.json()
    url = comics_img['img']
    img_path = download_img(url, save_dir)
    img_comment = comics_img['alt']

    return {'path': img_path, 'comment': img_comment}


def get_last_comic() -> int:
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()

    last_num = response.json()['num']

    return last_num


def get_upload_url(token: str, group_id: str, version_api: str) -> str:
    payload = {'access_token': token, 'group_id': group_id, 'v': version_api}
    url = 'https://api.vk.com/method/photos.getWallUploadServer'

    response = requests.get(url, params=payload)
    response.raise_for_status()

    upload_server_url = response.json()['response']['upload_url']

    return upload_server_url


def upload_img(url: str, file_path: str) -> dict:
    with open(file_path, 'rb') as image:
        files = {'photo': image}
        response = requests.post(url, files=files)
    response.raise_for_status()

    return response.json()


def save_img(token: str, group_id: str, version_api: str, upload_data: dict) -> dict:
    payload = {
        'access_token': token,
        'group_id': group_id,
        'photo': upload_data['photo'],
        'server': upload_data['server'],
        'hash': upload_data['hash'],
        'v': version_api}
    url = 'https://api.vk.com/method/photos.saveWallPhoto'

    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.json()['response'][0]


def post_img(token: str, group_id: str, version_api: str, save_data: dict, comment: str):
    payload = {
        'access_token': token,
        'owner_id': -int(group_id),
        'from_group': 1,
        'attachments': f'photo{save_data["owner_id"]}_{save_data["id"]}',
        'message': comment,
        'v': version_api}
    url = 'https://api.vk.com/method/wall.post'

    response = requests.get(url, params=payload)
    response.raise_for_status()


def delete_img(path: str) -> None:
    os.remove(path)


if __name__ == '__main__':
    load_dotenv()
    client_id = os.environ['VK_CLIENT_ID']
    group_id = os.environ['VK_GROUP_ID']
    token = os.environ['VK_TOKEN']
    version_api = os.environ['VK_V_API']

    message_contents = download_comics_img(DIR_IMG_XKCD)

    try:
        upload_url = get_upload_url(token, group_id, version_api)
        server_upload_resources = upload_img(upload_url, message_contents['path'])
        album_resources = save_img(token, group_id, version_api, server_upload_resources)
        post_img(token, group_id, version_api, album_resources, message_contents['comment'])
    finally:
        delete_img(message_contents['path'])
