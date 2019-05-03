from urllib.request import urlopen


# 获取豆瓣读书网页
def get_douban_book_img(page):
    j = 0
    for i in range(page):
        with urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}'.format(int(i) * 20)) as book:
            for line in book.readlines():
                line = line.decode('utf-8').strip()
                if 'img class=""' in line:
                    url = line[len('<img class="" src="'):-1]
                    name = url[len('https://img3.doubanio.com/view/subject/m/public/'):len(url)]
                    j += 1
                    print(url, j)
                    with urlopen(url) as img:
                        with open('../douban_img/' + name, 'wb') as local_img:
                            local_img.write(img.read())


if __name__ == '__main__':
    get_douban_book_img(50)
