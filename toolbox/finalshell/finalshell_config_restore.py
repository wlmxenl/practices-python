import os
import shutil
import zipfile

# FinalShell 还原配置从备份目录到安装目录
# conn 服务器连接信息配置文件夹
# config.json 基本配置文件
# knownhosts.json 服务器密钥
# tconfig.json 一些缓存
config_list = ('conn', 'config.json', 'knownhosts.json', 'tconfig.json')
# 备份文件名
backup_filename = 'finalshell_config.zip'


def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


if __name__ == "__main__":
    # FinalShell 安装目录
    install_dir_path = ""
    # FinalShell 配置备份目录
    backup_dir_path = ""

    assert len(install_dir_path) > 0, "未配置安装目录"
    assert len(backup_dir_path) > 0, "未配置备份目录"

    # 删除本地配置
    for item in config_list:
        filepath = os.path.join(install_dir_path, item)

        if os.path.exists(filepath):
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)

    # 解压配置至安装目录
    backup_file_path = os.path.join(backup_dir_path, backup_filename)
    with zipfile.ZipFile(backup_file_path, 'r') as zip_ref:
        zip_ref.extractall(install_dir_path)

    print("备份目录: %s" % backup_dir_path)
    print("安装目录: %s" % install_dir_path)
    print("恢复完成")