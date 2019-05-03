import os

# open(file, mode)
# mode: r读、a追加、w写、x创建、t文件、b二进制 默认mode是rt 注意：x模式是独占模式，如果文件存在则报错
# 注意：open函数的相对路径是相对于python文件的 当有中文字符时使用encoding='utf-8'参数


# 读
# 按字符读 使用with as 会自动释放资源
import platform
import shutil
from urllib.request import urlopen

with open('../work/news.txt', encoding='utf-8') as f:
    print(f.read())
# 指定字符数
with open('../work/news.txt', encoding='utf-8') as f:
    print(f.read(6))

# 按行读
with open('../work/news.txt', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
    print('-------------------------------------------')
with open('../work/news.txt', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())

# 网络文件 decode()表示解码
with urlopen('https://mail.yeah.net') as f:
    for line in f.readlines():
        print(line.decode('utf-8').strip())


# 写
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('hello, 你好啊！')

# 追加写
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('hello, 你好啊！')


# 二进制文件的读写
with open('image.jpeg', 'rb') as f:
    with open('image.jpg', 'wb') as new_f:
        new_f.write(f.read())


# 文件夹和文件 os模块

# os模块
# 系统类型
print(os.name)

# window下获取系统信息
print(platform.uname())

# 系统环境信息
print(os.environ)
print(os.environ.get('PATH'))


# 文件操作
# 文件存在则删除
if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('file not exists')

# 重命名
if os.path.exists('new.jpg'):
    os.remove('new.jpg')
os.rename('image.jpg', 'new.jpg')

# copy
shutil.copy('new.jpg', 'new1.jpg')
