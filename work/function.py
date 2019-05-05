from functools import reduce


# 1. 统计大小写字母个数
def statistics(string):
    upper_count = 0
    lower_count = 0
    for elem in string:
        if elem.isupper():
            upper_count += 1
        elif elem.islower():
            lower_count += 1
    return upper_count, lower_count


# list 去重 乱序
def repeat_rid(name):
    new = list(set(name))
    return new


# list 去重 还是以前顺序
def repeat_rid_order(name):
    new = list(set(name))
    new.sort(key=name.index)
    return new


# 斐波那契数列
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# 汉诺塔
def hanoi(n, start, go, end):
    if n == 1:
        print('{} -> {}'.format(start, end))
    else:
        hanoi(n - 1, start, end, go)
        hanoi(1, start, go, end)
        hanoi(n - 1, go, start, end)


# 杨辉三角
def triangles(n):
    # 杨辉三角形的数
    def triangles_num(line, col):
        # 每行第一个和最后一个为1
        if col == 0 or line == col:
            return 1
        else:
            # 上边两个数相加
            return triangles_num(line - 1, col - 1) + triangles_num(line - 1, col)
    # 画图
    for i in range(0, n):
        # 画空格
        for x in range(1, n - i):
            print(end=" ")
        # 杨辉三角形数
        for j in range(0, i + 1):
            print(triangles_num(i, j), end=" ")
        print()


# 参数组合
def all_parameter(name, password, national='汉', *hobby, age, married=False, **kw):
    return name, password, national, hobby, age, married, kw


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
    print(statistics('TuTyn./'))
    print(repeat_rid([2, 8, 5, 9, 8, 9, 2]))
    print(repeat_rid_order([2, 8, 5, 9, 8, 9, 2]))
    print(fibonacci(10))
    hanoi(2, 'A', 'B', 'C')
    triangles(9)
