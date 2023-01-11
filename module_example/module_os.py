# https://docs.python.org/zh-cn/3.11/library/os.html
import getpass
import os


# print(os.getlogin()) # 返回通过控制终端进程进行登录的用户名
# print(getpass.getuser()) # 在多数情况下，推荐使用此方法获取用户名


# print(os.environ) # 系统环境变量 mapping 对象
# print(os.getenv('PATH')) # 返回 PATH 环境变量字符串


# print(os.getcwd()) # 返回表示当前工作目录的字符串
# print(os.listdir(os.getcwd())) # 返回指定目录中条目名称组成的列表
# print(os.listdir('module_example'))


# os.mkdir('test') # 创建 test 目录，如果父目录不存在会报异常
# os.makedirs('test/dir/subdir') # 递归创建目录
# os.removedirs('test/dir/subdir') 递归删除目录
# os.remove('test/t.txt') # 删除文件，文件不存在抛出异常
# os.renames('test/dir/subdir', 'test2/dir2/subdir2') # 递归重命名目录或文件, 除了会首先创建新路径所需的中间目录。重命名后，将调用 removedirs() 删除旧路径中不需要的目录。
# os.replace('test3/dir3/subdir', 'test3/dir3/subdir3') # 将文件或目录 src 重命名为 dst
# os.rmdir('test3/dir3/subdir3') # 只删除 subdir3 目录


# os.scandir(), 返回一个 os.DirEntry 对象的迭代器
# 如果需要文件类型或文件属性信息，使用 scandir() 代替 listdir() 
# with os.scandir() as it:
#     for entry in it:
#         print(entry)


# print(os.curdir) # 当前目录的常量字符串。在 Windows 和 POSIX 上是 '.'。
# print(os.pardir) # 目录的常量字符串。在 Windows 和 POSIX 上是 '..'。
# print(os.sep) # 在 POSIX 上是 '/'，在 Windows 上是是 '\\'。


# print(os.urandom(6)) # 返回大小为 size 的字节串，它是适合加密使用的随机字节。