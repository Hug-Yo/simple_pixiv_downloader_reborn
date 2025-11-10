from typing import List
from model import ArtWorks
from crud import pending_artworks,artworks
from headers import HEADERS
import requests
from enum import Enum

class PopInfo(Enum):
    LIKE = '喜欢'
    BOOKMARKS = '订阅'
    VIEW = '浏览'

def get_multiple_pages(url,pages: str) -> list:
    url_list = []
    ...
    return url_list

def save_artwork(res: requests.Response,addr):
    with open(addr,"wb") as file:
        file.write(res.content)

def download_artworks(url: str,pages: str) -> None:
    if pages != '1':
        #若为多页作品则启用url多页处理
        multi_url = get_multiple_pages(url,pages)
        for url in multi_url:
            res = requests.get(url, headers=HEADERS)
            #保存文件(调用save_artwork函数)
        ...
    else:
        res = requests.get(url,headers=HEADERS)
        #保存文件
        ...

def general_download(artwork_list: List[ArtWorks],dependence: PopInfo,min_limit) -> None:
    for artwork in artwork_list:
        if dependence == PopInfo.LIKE:
            if artwork.likes >= min_limit:
                download_artworks(artwork.url,artwork.pages)
    for artwork in artwork_list:
        if dependence == PopInfo.BOOKMARKS:
            if artwork.bookmarks >= min_limit:
                download_artworks(artwork.url,artwork.pages)
    for artwork in artwork_list:
        if dependence == PopInfo.VIEW:
            if artwork.views >= min_limit:
                download_artworks(artwork.url,artwork.pages)


