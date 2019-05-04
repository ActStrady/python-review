import os
from urllib.request import urlopen


# 获取豆瓣读书网页
def get_douban_book_img(page):
    # 创建图片存储文件夹
    path = '../douban_img/'
    if not os.path.exists(path):
        os.makedirs(path)
    # 获取豆瓣读书网页
    for i in range(page):
        with urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}'.format(int(i) * 20)) as f:
            for line in f.readlines():
                line = line.decode('utf-8').strip()
                # 找图片特征，截取图片url
                if 'img class=""' in line:
                    # 图片url
                    url = line[len('<img class="" src="'):-1]
                    # 图片名
                    name = url[len('https://img3.doubanio.com/view/subject/m/public/'):len(url)]
                    # 写入本地
                    with urlopen(url) as img:
                        with open(path + name, 'wb') as local_img:
                            local_img.write(img.read())


if __name__ == '__main__':
    get_douban_book_img(5)
