"""
启动 [NeatDownloadManager](https://www.neatdownloadmanager.com/) 批量下载文件
"""
import os
import subprocess
import time


# 当前文件夹下载列表文件
url_file_path = "url_list.txt"
# 启动下载间隔时间, 单位秒
interval_download_time = 2 * 60


def download_with_ndm(url):
    subprocess.run([os.path.join(os.getenv('NDM_INSTALL_PATH'), 'NeatDM.exe'), url])
    pass


def set_downloaded_flag(url):
    with open(url_file_path, "r") as f:
        filedata = f.read()
    filedata = filedata.replace(url, "#" + url)
    with open(url_file_path, "w") as f:
        f.write(filedata)
    pass


def read_download_url():
    with open(url_file_path, 'r') as f:
        for line in f:
            url = line.strip()
            if url.startswith("http"):
                return url
    return ""


if __name__ == '__main__':
    assert os.getenv('NDM_INSTALL_PATH') is not None, "读取 NDM 安装目录失败"

    while True:
        download_url = read_download_url()
        print("--> " + download_url)
        if len(download_url) == 0:
            break
        download_with_ndm(download_url)
        set_downloaded_flag(download_url)
        time.sleep(interval_download_time)

    print("Completed!")
