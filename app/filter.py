#链式调用筛选结果
from model import ArtWorks
from crud import pending_artworks,artworks
from typing import List

class ArtworkFilter:
    def __init__(self,artworks_list: List[ArtWorks]):
        self.artworks_list = artworks_list

    def by_likes(self):
        self.artworks_list.sort(key=lambda artwork: artwork.likes, reverse=True)
        return self

    def by_bookmarks(self):
        self.artworks_list.sort(key=lambda artwork: artwork.bookmarks, reverse=True)
        return self

    def by_views(self):
        self.artworks_list.sort(key=lambda artwork: artwork.views, reverse=True)
        return self

    def all(self) -> List[ArtWorks]:
        return self.artworks_list

    def limited(self,limit: str) -> List[ArtWorks]:
        if eval(limit) >= len(self.artworks_list):
            return self.artworks_list
        else:
            return self.artworks_list[:limit]