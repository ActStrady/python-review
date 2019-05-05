from functools import reduce

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


# 函数参数
# 位置参数 与其他语言类似
# 默认参数 默认参数放在位置参数之后，变化小的作为默认参数，默认参数不能为可变的对象
# 调用时：默认参数如果写参数名则可以乱序调用 可以不写参数调用
def mut(x, y=2, z=5):
    return x * y * z


# 可变参数 使用 * + 参数名 实际上被封装为一个元组 可以不写参数调用
def variable(*args):
    return args


# 关键字参数 使用** + 参数名来定义，一般定义为kw 会被组装为一个字典 传入key=value格式 可以不写参数调用
def kv(**kw):
    return kw


# 命名关键字参数 *, + 参数名来定义, 要传入规定的的参数，不可以不写参数
def named_kv(*, age, married=False):
    return age, married


# 当有可变参数的时候可以不写*
def named_kv_var(*args, age, married=False):
    return args, age, married


# 参数组合 顺序：位置参数，默认参数，可变参数，命名关键字参数，关键字参数
def all_parameter(name, password, national='汉', *hobby, age, married=False, **kw):
    return name, password, national, hobby, age, married, kw


# 高阶函数 函数式编程的产物，就是说该函数有参数是函数，函数可以作为参数来传递
# 几个内置的高阶函数
# map函数，两个参数，一个函数，一个序列，用来把函数用到每一个序列成员
nums = (4, 5, 8, -8, 9, -7)
print(tuple(map(abs, nums)))


# reduce函数 首先参数函数必须只有两个参数，把结果继续和序列的下个元素累积
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def power(num, p=2):
    return num ** p


print(reduce(power, (2, 2, 2, 2)))


# filter函数 参数函数必须返回布尔，根据布尔值来决定元素去留
def positive(num):
    return num >= 0


print(list(filter(positive, nums)))

# sorted函数， key=可以指定排序的函数
print(sorted(nums))
# 下面的lambda表达式表示一个函数：输入一个值然后取其绝对值，根据绝对值来排序
print(sorted(nums, key=lambda x: abs(x)))

if __name__ == '__main__':
    prt(add(1, 2))
    prt(get(1, 2))
    prt(sub(2, 2.3))
    # prt(sub(3, '5'))

    # 默认参数写参数名可以乱序调用
    prt(mut(2, z=6, y=7))
    # 默认参数不传值
    prt(mut(2))

    # 可变参数传入一个列表
    prt(variable(*[4, 5, 6, 8, 9]))
    # 可变参数不传值
    prt(variable())

    # 关键字参数
    prt(kv(name='perter', age=18))
    # 关键字参数不传值
    prt(kv())

    # 命名关键字参数
    prt(named_kv(age=25))
    prt(named_kv_var(2, 5, 8, age=36, married=True))

    # 全部参数
    prt(all_parameter('张衡', '12456', '维吾尔', '唱', '跳', '篮球', age=20, good_at='鸡你太美'))
