import os
import urllib.parse
from pathlib import Path

import requests


def download_img(img_url: str, save_path: str):
    Path(save_path).mkdir(parents=True, exist_ok=True)
    img_name = search_full_name_img(img_url)

    response = requests.get(img_url)
    response.raise_for_status()

    img_save_path = f'{save_path}/{img_name}'

    with open(img_save_path, 'wb') as file:
        file.write(response.content)

    return img_save_path


def search_full_name_img(url: str) -> str:
    img_url = urllib.parse.urlsplit(url).path
    unquote_img_url = urllib.parse.unquote(img_url)
    img_file = os.path.split(unquote_img_url)[-1]
    name_img = "".join(os.path.splitext(img_file))

    return name_img
