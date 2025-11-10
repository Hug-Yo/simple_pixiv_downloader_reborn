#要实现能从文件中读取并判断上次程序推出后是否下载完成，实现程序可间断运行
#因此此文件涉及文件的写入与读写操作

import os
from model import ArtWorks
from typing import List
import json

#初始化全局变量列表
artworks: List[ArtWorks] = []
pending_artworks: List[ArtWorks] = []
def init() -> None:
    global artworks, pending_artworks
    #从文件读取数据，判断哪些作品没有处理完毕
    # 1. 获取当前脚本 (crud.py) 所在的目录绝对路径
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)

    # 2. 从 crud.py 所在目录 (app) 导航至目标文件
    # 思路: app -> 跳出app目录 -> 进入data目录 -> 进入下级data目录 -> 找到download_data.json
    parent_dir = os.path.dirname(current_dir)  # 跳到与app同级的目录
    data_file_path = os.path.join(parent_dir, 'data', 'data', 'download_data.json')
    with open(data_file_path, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
        pending_artworks = loaded_data["pending_artworks"]
        artworks = loaded_data["artworks"]


def save_artwork() -> None:
    #将列表数据写入文件
    # 从文件读取数据，判断哪些作品没有处理完毕
    # 1. 获取当前脚本 (crud.py) 所在的目录绝对路径
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)

    # 2. 从 crud.py 所在目录 (app) 导航至目标文件
    # 思路: app -> 跳出app目录 -> 进入data目录 -> 进入下级data目录 -> 找到download_data.json
    parent_dir = os.path.dirname(current_dir)  # 跳到与app同级的目录
    data_file_path = os.path.join(parent_dir, 'data', 'data', 'download_data.json')
    with open(data_file_path, 'w+', encoding='utf-8') as file:
        data_to_save = {
            "pending_artworks": pending_artworks,
            "artworks": artworks
        }
        json.dump(data_to_save, file, ensure_ascii=False, indent=4)
    ...