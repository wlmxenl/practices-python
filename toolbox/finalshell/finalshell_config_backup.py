import os
import shutil

# FinalShell 备份配置文件到指定目录
# conn 服务器连接信息配置文件夹
# config.json 基本配置文件
# knownhosts.json 服务器密钥
# tconfig.json 一些缓存
backup_files = ('conn', 'config.json', 'knownhosts.json', 'tconfig.json')

if __name__ == "__main__":
    # FinalShell 安装目录
    install_dir_path = os.getenv('FS_INSTALL_PATH')
    # FinalShell 配置备份目录
    backup_dir_path = os.getenv('FS_BACKUP_PATH')

    assert install_dir_path is not None, "无效的安装目录"
    assert backup_dir_path is not None, "无效的备份目录"

    # 备份配置
    for item in backup_files:
        src_path = os.path.join(install_dir_path, item)
        dst_path = os.path.join(backup_dir_path, item)
        if os.path.isdir(src_path):
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copyfile(src_path, dst_path)

    print("备份目录: %s" % backup_dir_path)
    print("安装目录: %s" % install_dir_path)
    print("备份完成")
