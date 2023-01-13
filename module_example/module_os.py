# https://docs.python.org/zh-cn/3.11/library/os.html
# https://docs.python.org/zh-cn/3.11/library/os.path.html
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


# print(os.path.abspath('module_example')) # 返回路径 path 的绝对路径
# print(os.path.dirname(os.getcwd())) # 返回路径 path 所在目录
# print(os.path.exists('.gitignore')) # 文件是否存在
# print(os.path.getsize('.gitignore')) # 返回 path 的大小，以字节为单位
# print(os.path.isabs(os.getcwd())) # 如果 path 是一个绝对路径，则返回 True
# print(os.path.isfile('.gitignore'))
# print(os.path.isdir('module_example'))
# print(os.path.join(os.getcwd(), 'test')) 路径拼接
# print(os.path.normcase('D:/Program Files')) # d:\program files, 规范路径的大小写。在 Windows 上，将路径中的所有字符都转换为小写，并将正斜杠转换为反斜杠。在其他操作系统上返回原路径。
# print(os.path.normpath('D://Program Files')) # D:\Program Files, 通过折叠多余的分隔符和对上级目录的引用来标准化路径名
# print(os.path.relpath('module_example', start=os.curdir)) # 返回从当前目录或可选的 start 目录至 path 的相对文件路径
# print(os.getcwd(), os.path.split(os.getcwd())) # D:\DevWorkspace\VSCodeProject\practices-python ('D:\\DevWorkspace\\VSCodeProject', 'practices-python')
# print(os.path.splitext('module_example/module_os.py')) # ('module_example/module_os', '.py'), 分离文件名和拓展名
# print(os.path.basename('module_example/module_os.py')) # module_os.py, 提取文件名