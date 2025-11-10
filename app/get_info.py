import requests
from crud import artworks,pending_artworks
from app.model import ArtWorks
from headers import HEADERS
from typing import List
from config import *
import json
import re

def get_ranking_url(pages: str) -> None:
    base_url = ' '
    res = requests.get(base_url, headers=HEADERS)
    #处理结果获取作品url

    # 得到url后创建ArtWork对象，并将画作添加到pending_artwork列表中

#获取单页搜索结果信息，pages为页码
def get_search_url(pages: str) -> None:
    base_url = f'https://www.pixiv.net/ajax/search/illustrations/{s_tags}?word={s_tags}&order={s_order}&mode={s_age_mode}&p={pages}&csw=0&s_mode=s_tag&type={s_type}&lang=en'
    res = requests.get(base_url, headers=HEADERS)
    #处理结果获取作品url
    result = json.loads(res.text)
    for item in result['body']['illust']['data']:
        pid = item['id']
        url = re.sub(r'/c/\d+x\d+_\d+_a\d+/|square1200',
                 lambda m: '/' if 'c/' in m.group(0) else 'master1200',
                 item['url'])
        title = item['title']
        userid = item['userId']
        pages = item['pageCount']
    # 得到url后创建ArtWork对象，并将画作添加到pending_artwork列表中
        pending_artworks.append(ArtWorks(pid,url,title,userid,None,None,None,pages))

def get_users_url(pages: str) -> None:
    base_url = ' '
    res = requests.get(base_url, headers=HEADERS)
    #处理结果获取作品url

    #得到url后创建ArtWork对象，并将画作添加到pending_artwork列表中

def handle_pending_artworks(artworks_list: List[ArtWorks]) -> None:
    for artwork in artworks_list:
        #解析res获取画作信息，将作品添加到artworks列表中，删除pending_artwork中的此对象
        url = f'https://www.pixiv.net/ajax/illust/{artwork.pid}'
        res = requests.get(url, headers=HEADERS)
        result = json.loads(res.text)
        likes = result['body']['likeCount']
        views = result['body']['viewCount']
        bookmarks = result['body']['bookmarkCount']
        artwork.likes = likes
        artwork.views = views
        artwork.bookmarks = bookmarks
        artworks.append(artwork)
        pending_artworks.remove(artwork)
        break
