#定义需要的类


class ArtWorks:
    #定义画作的类，爬取时先抓取作品url创建类，其余值默认为空
    def __init__(self,
                 pid: str,
                 url: str,
                 title: str | None = None,
                 userid:str | None = None,
                 likes: str | None = None,
                 bookmarks: str | None = None,
                 views: str | None = None,
                 pages: str | None = None,
                 downloaded: bool = False,):
        self.pid: str | None = pid
        self.url: str = url
        self.title: str | None = title
        self.userid: str | None = userid
        self.likes: str | None = likes
        self.bookmarks: str | None = bookmarks
        self.views: str | None = views
        self.pages: str | None = pages
        self.downloaded: bool = downloaded

