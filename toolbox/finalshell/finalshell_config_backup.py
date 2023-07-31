import os
import zipfile

# FinalShell 备份配置文件到指定目录
# conn 服务器连接信息配置文件夹
# config.json 基本配置文件
# knownhosts.json 服务器密钥
# tconfig.json 一些缓存
config_list = ('conn', 'config.json', 'knownhosts.json', 'tconfig.json')
# 备份文件名
backup_filename = 'finalshell_config.zip'


def compress_config_files(zip_filename, backup_files):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in backup_files:
            if os.path.isfile(item):
                zipf.write(item, os.path.basename(item))
            elif os.path.isdir(item):
                for root, _, files in os.walk(item):
                    for file in files:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, item)
                        zipf.write(file_path, os.path.join(os.path.basename(item), relative_path))


if __name__ == "__main__":
    # FinalShell 安装目录
    install_dir_path = ""
    # FinalShell 配置备份目录
    backup_dir_path = ""

    assert len(install_dir_path) > 0, "未配置安装目录"
    assert len(backup_dir_path) > 0, "未配置备份目录"

    config_files = [os.path.join(install_dir_path, item) for item in config_list]
    compress_config_files(os.path.join(backup_dir_path, backup_filename), config_files)

    print("备份目录: %s" % backup_dir_path)
    print("安装目录: %s" % install_dir_path)
    print("备份完成")
