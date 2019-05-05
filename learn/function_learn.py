from work.file import long_word

# 其实python中的函数也是对象，所以函数也可以进行赋值
prt = print
prt('函数名是指向一个函数对象的引用')

# 导函数 见上边的from一行
prt(long_word('../work/news.txt'))


# 空函数 使用pass
def empty():
    pass


# 函数文档注释 python的函数文档注释是写在函数里面最开始的
def add(x, y):
    """
    加法运算
    :param x: 数值1
    :param y: 数值2
    :return: 和
    """
    return x + y


# 返回多参数 实际上是被封装为一个元组
def get(x, y):
    return x, y


# 函数的异常处理 raise 抛出异常
def sub(x, y):
    """
    减法运算
    :param x: 减数
    :param y: 被减数
    :return: 差
    """
    if not isinstance(x, (int, float)):
        raise TypeError('减数必须是数值')
    if not isinstance(y, (int, float)):
        raise TypeError('被减数必须是数值')
    return x - y


if __name__ == '__main__':
    prt(add(1, 2))
    prt(get(1, 2))
    prt(sub(2, 2.3))
    prt(sub(3, '5'))
