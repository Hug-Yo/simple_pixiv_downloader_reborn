from typing import List

from config import s_tags, s_age_mode
from model import ArtWorks
from crud import pending_artworks,artworks
from headers import HEADERS
import requests
from enum import Enum
import os

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

def download_artworks(url: str,pages: str,pid: str) -> None:
    #下载
    file_addr = get_download_path()
    if str(pages) != '1':
        #若为多页作品则启用url多页处理
        count = 1
        multi_url = get_multiple_pages(url,pages)
        for url in multi_url:
            res = requests.get(url, headers=HEADERS)
            addr = os.path.join(file_addr, pid, f'{str(count)}.png')
            count += 1
            # 保存文件(调用save_artwork函数)
            save_artwork(res,addr)

    else:
        res = requests.get(url,headers=HEADERS)
        #保存文件
        addr = os.path.join(file_addr, f'{pid}.png')
        save_artwork(res, addr)

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

def get_download_path():
    # 获取文件路径
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)  # app目录
    dir_name = f'{s_tags}_{s_age_mode}'
    # 构建artworks目录下的目标目录路径
    parent_dir = os.path.dirname(current_dir)  # 项目根目录
    target_dir = os.path.join(parent_dir, 'data', 'artworks', dir_name)
    # 检查目录是否存在，不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)  # exist_ok=True 避免目录已存在时报错
    return target_dir
