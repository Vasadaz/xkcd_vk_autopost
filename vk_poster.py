import requests

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
    download_comics_img(DIR_IMG_XKCD)
