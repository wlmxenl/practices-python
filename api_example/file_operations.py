import os

def readFile():
    # 文件读取
    # r  以只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式
    # r+ 可读写
    with open('assets/lipsum.txt', 'r') as f:
        # print(f.read()) # 读取全部内容
        # print(f.readline()) # 读取一行
        for line in f.readlines():
            print(line)

def writeFile():
    # 文件写入
    # w  打开一个文件只用于写入，如果该文件已存在则将其覆盖。如果该文件不存在，则创建新文件。
    # w+ 可读写
    with open('tmp/file_write.txt', 'w') as f:
        f.write('Python')

def appendTextToFile():
    # 文件写入，追加模式
    # a 打开一个文件用于增加, 如果该文件已经存在，文件指针将会放在文件的结尾。如果该文件不存在，则创建新文件进行写入。
    # a+ 可读写
    with open('tmp/file_append.txt', 'a') as f:
        for i in (range(0, 10)):
            f.write(str(i))
            f.write('\n')

def readFileWithSeek():
    with open('assets/lipsum.txt', 'r') as f:
        # seek(offset, from)
        # 参数 offset 偏移量单位字节，负数是往回偏移，正数是往前偏移，
        # from位置：0表示文件的开头，1表示当前位置，2表示文件末尾
        f.seek(10, 0)
        print(f.read(10)) # 从指定文件指针开始读取10个字符


def testFlush():
    """
    flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
    一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
    """
    file = open('tmp/file_flush.txt', 'w')
    file.write('hello')
    file.flush()
    file.write('world')
    file.close()

if __name__ == '__main__':
    if not os.path.exists('tmp'):
      os.mkdir('tmp')
      
    testFlush()