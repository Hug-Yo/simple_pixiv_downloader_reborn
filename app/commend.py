from model import ArtWorks
from downder import *
from get_info import *
from model import *

get_search_url('1')
handle_pending_artworks(pending_artworks)
for artwork in artworks:
    download_artworks(artwork.url, artwork.pages, artwork.pid)

