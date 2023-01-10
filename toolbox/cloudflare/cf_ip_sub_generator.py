"""
使用 cf中转ip 生成 v2rayN 格式订阅
中转ip文件来源：https://t.me/cf_push
"""
import csv
import glob
import os.path
import re
import subprocess
import base64
import configparser
import json


def is_valid_ipv4(ip: str):
    pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
    return re.match(pattern, ip) is not None


def get_ip_from_file_txt(fpath):
    cf_ip_set = set()
    with open(fpath, 'r') as f1:
        for cip in f1:
            if is_valid_ipv4(cip.strip()):
                cf_ip_set.add(cip.strip())
    return cf_ip_set


def get_ip_from_iptest(min_speed):
    ip_list = list()
    with open('iptest/ip.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            if int(re.findall(r"\d+", row[6])[0]) > min_speed:
                ip_list.append(row[0])
    return ip_list


if __name__ == '__main__':
    # 从频道导出文件的输出目录
    cf_ip_folder_path = r"C:\Users\Administrator\Downloads\Telegram Desktop\ChatExport_2023-03-24\files"
    # 合并文件输出文件名
    output_file_path = "ip.txt"
    # 测速最大 ip 数, 全部导出可能有10w+ ip
    max_iptest_count = 2000

    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # 去重后的 ip 集合
    all_ips = set()

    # 读取所有 .txt 文件路径
    file_list = glob.glob(os.path.join(cf_ip_folder_path, "*.txt"))
    for file_path in file_list:
        # 指定 443 端口的文件
        if file_path.__contains__("443"):
            all_ips.update(get_ip_from_file_txt(file_path))

    # 输出 ip 到指定文件
    ip_count = 0
    with open(output_file_path, "a+") as f:
        for item in all_ips:
            f.write(item)
            ip_count += 1
            if ip_count == max_iptest_count:
                break
            f.write("\n")

    # ip 测速
    iptest_cmd = "cd iptest && iptest-windows-amd64.exe -file ../{}".format(output_file_path)
    subprocess.run(iptest_cmd, shell=True)

    # 提取测速大于5M的 ip
    final_ip_list = get_ip_from_iptest(5000)

    # 生成订阅文件
    config = configparser.ConfigParser()
    config.read("cf_config.ini", encoding='utf-8')
    vmess_url = config.get('SERVER', 'vmess_ws_url')
    subscribe_list = list()

    for index, ip in enumerate(final_ip_list):
        node_config_json = json.loads(str(base64.b64decode(vmess_url[8:]), 'utf-8'))
        node_config_json['add'] = ip
        node_config_json['ps'] = config.get('SERVER', 'subscribe_node_name') + "{}".format(index)
        subscribe_list.append("vmess://" + str(base64.b64encode(json.dumps(node_config_json).encode('utf-8')), 'utf-8'))

    with open(config.get('SERVER', 'subscribe_file_name'), 'w', encoding='utf-8') as f:
        f.write(str(base64.b64encode('\n'.join(subscribe_list).encode('utf-8')), 'utf-8'))

    print("finished")

