import platform
import time
import math

# 保留格式输出
print('''
        登 鹳 雀 楼
        - 【唐】王之涣

        白日依山尽，
        黄河入海流。
        欲穷千里目，
        更上一层楼。
    ''')

# 当前的python版本
print(platform.python_version())

# 格式化输出当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 圆面积
def area(r):
    return math.pi * r ** 2


'''
    digit 含义时数字 位数字 
    numeric 含义时数字
    decimal 含义是十进制
    isdigit() isnumeric() isdecimal() 的区别
    1. isdigit可以判定阿拉伯数字和byte数字
              不可判定罗马数字和汉字数字
    2. isnumeric可以判定阿拉伯数字和汉字以及罗马数字
                但没有判定byte数字的方法
    3. isdecimal可以判定阿拉伯数字
                不可以判定罗马数字和汉字数字
                也没有判定byte数字的方法
'''


# 判定区别的方法
def num_diff():
    num = '1'
    print('阿拉伯数字isdigit()', num.isdigit())
    print('阿拉伯数字isnumeric()', num.isnumeric())
    print('阿拉伯数字isdecimal()', num.isdecimal())

    num = 'Ⅰ'
    print('罗马数字isdigit()', num.isdigit())
    print('罗马数字isnumeric()', num.isnumeric())
    print('罗马数字isdecimal()', num.isdecimal())

    num = '一'
    print('汉字数字isdigit()', num.isdigit())
    print('汉字数字isnumeric()', num.isnumeric())
    print('汉字数字isdecimal()', num.isdecimal())

    num = b'1'
    print('byte数字isdigit()', num.isdigit())

    # 没这方法
    # print('byte数字isnumeric()', num.isnumeric())
    # print('byte数字isdecimal()', num.isdecimal())


if __name__ == '__main__':
    print('请输入半径:')
    print('面积为:{}'.format(area(int(input()))))
    num_diff()
