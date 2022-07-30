import requests

from downloader import download_img


DIR_IMG_XKCD = 'comics_xkcd'

def download_comics_img(save_dir: str):
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    launches = response.json()
    url = launches['img']
    download_img(url, save_dir)


if __name__ == '__main__':
    download_comics_img(DIR_IMG_XKCD)
