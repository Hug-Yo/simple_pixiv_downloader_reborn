#实现函数具体功能

from typing import List
from filter import ArtworkFilter
from model import ArtWorks
from crud import artworks,pending_artworks

def by_bookmarks():
    return ArtworkFilter(artworks).by_bookmarks().all()

def by_likes():
    return ArtworkFilter(artworks).by_likes().all()

def by_views():
    return ArtworkFilter(artworks).by_views().all()

