# https://docs.python.org/zh-cn/3/library/sys.html
import sys


# 查看 python 版本号
# https://docs.python.org/zh-cn/3/library/sys.html#sys.version_info
print(sys.version_info)


# 查看平台标识符
# https://docs.python.org/zh-cn/3/library/sys.html#sys.platform
# Windows -> win32
# Windows/Cygwin -> cygwin
# macOS -> darwin
print(sys.platform)


print("数字 24 占用的内存大小为 {} 个字节".format(sys.getsizeof(24)))