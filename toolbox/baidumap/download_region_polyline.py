import json
import os
import requests


class RegionInfo:
    def __init__(self, data):
        self.code = data.get("code", "")
        self.name = data.get("name", "")
        self.level = data.get("level", 0)
        self.districts = [RegionInfo(item) for item in data.get("districts", [])]


def traverse_region_list(region_list, block):
    for region_item in region_list:
        block(region_item)
        if len(region_item.districts) > 0:
            traverse_region_list(region_item.districts, block)
    pass


def print_region_info(region_info):
    print(" " * region_info.level * 2, region_info.name, region_info.code)
    pass


def parse_region_data():
    with open("china_region.json", "r", encoding="utf-8") as file:
        return [RegionInfo(item) for item in json.load(file)]
    pass


def download_polyline_data(region_info):
    ak = ""
    # 文件保存目录
    save_dir = os.path.join(os.getcwd(), "tmp_polyline_data")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    # 拼接保存文件的路径
    save_path = os.path.join(save_dir, f"{region_info.code}.json")
    # 跳过已下载
    if os.path.exists(save_path):
        print(save_path)
        return
    # 下载文件
    url = f"https://api.map.baidu.com/api_region_search/v1/?keyword={region_info.code}&sub_admin=0&extensions_code=1&boundary=1&ak={ak}"
    print(url)
    response = requests.get(url)
    assert response.status_code == 200, response.reason
    with open(save_path, "w", encoding="utf-8") as file:
        json.dump(response.json(), file, ensure_ascii=False)
    pass


if __name__ == '__main__':
    china_region_list = parse_region_data()

    # 输出行政数据信息
    # traverse_region_list(china_region_list, print_region_info)

    # 下载边界数据
    traverse_region_list(china_region_list, download_polyline_data)
    pass
