import json
import os
import re
import sqlite3
import requests

polyline_save_dir = "D:\\bd_polyine"
ak = ""


class RegionInfo:
    def __init__(self, data):
        self.code = data.get("code", "")
        self.name = data.get("name", "")
        self.level = data.get("level", 0)
        self.districts = [RegionInfo(item) for item in data.get("districts", [])]
        self.polyline = ""


def traverse_region_list(region_list, block, parent_code="0"):
    for region_item in region_list:
        block(region_item, parent_code)
        if len(region_item.districts) > 0:
            traverse_region_list(region_item.districts, block, region_item.code)
    pass


def print_region_info(region_info, parend_code):
    print(" " * region_info.level * 2, region_info.name, region_info.code, parend_code)
    pass


def parse_region_data():
    with open("china_region.json", "r", encoding="utf-8") as file:
        return [RegionInfo(item) for item in json.load(file)]
    pass


def download_polyline_data(region_info):
    # 文件保存目录
    if not os.path.exists(polyline_save_dir):
        os.makedirs(polyline_save_dir)
    # 拼接保存文件的路径
    save_path = os.path.join(polyline_save_dir, f"{region_info.code}.json")
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


def load_polyline_info(region_info, parend_code):
    polyline_data_file_path = os.path.join(polyline_save_dir, f"{region_info.code}.json")
    assert os.path.exists(polyline_data_file_path), "polyline data not found"
    with open(polyline_data_file_path, 'r', encoding='utf-8') as file:
        polyline_data_json = json.load(file)
    polyline_data = polyline_data_json["districts"][0]["polyline"]

    data_type_pattern = r"^[^(]+"
    data_type_str = re.match(data_type_pattern, polyline_data).group()  # MULTIPOLYGON、POLYGON

    new_polyline_data = (polyline_data.replace(data_type_str, '').replace(')))', '')
                         .replace('(((', '')
                         .replace(')),((', '|')
                         .replace('),(', '|')
                         .replace('((', '')
                         .replace("))", ''))
    region_info.polyline = new_polyline_data

    # print(region_info.name, len(new_polyline_data.split('|')))
    # for sub_polyline_data in new_polyline_data.split('|'):
    #     lonlat_arr = sub_polyline_data.split(',')
    #     print(lonlat_arr[0], lonlat_arr[len(lonlat_arr) - 1])
    #     for lonlat in sub_polyline_data.split(','):
    #         print(lonlat)


def insert_region_info_to_db(cursor, region_info, parent_code):
    cursor.execute("INSERT INTO region_data (code, parent_code, name, level, center, polyline) VALUES (?, ?, ?, ?, ?, ?)",
                   (region_info.code, parent_code, region_info.name, region_info.level, '', region_info.polyline))
    pass


def save_data_to_sqlite(region_list):
    conn = sqlite3.connect('bd_region.db')
    cursor = conn.cursor()
    # 创建一个表
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS region_data (
                id INTEGER PRIMARY KEY,
                code INTEGER NOT NULL,
                parent_code INTEGER NOT NULL,
                name TEXT NOT NULL,
                level INTEGER NOT NULL,
                center TEXT DEFAULT NULL,
                polyline TEXT NOT NULL
            )
        ''')
    for region_item in region_list:
        insert_region_info_to_db(cursor, region_item, '0')
        if len(region_item.districts) > 0:
            for child_region_item in region_item.districts:
                insert_region_info_to_db(cursor, child_region_item, region_item.code)
        pass

    conn.commit()
    conn.close()
    pass


if __name__ == '__main__':
    china_region_list = parse_region_data()

    # 下载边界数据
    # traverse_region_list(china_region_list, download_polyline_data)

    # 读取边界信息
    # traverse_region_list(china_region_list, load_polyline_info)

    # 输出行政数据信息
    # traverse_region_list(china_region_list, print_region_info)

    # save_data_to_sqlite(china_region_list)
    pass
