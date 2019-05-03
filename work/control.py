from decimal import Decimal
import math


# 9. 一个数如果恰好等于它的因子之和，这个数就称为’完数’。例如6=1＋2＋3.编程 找出1000以内的所有完数。
def perfect_num():
    for i in range(1, 1001):
        sums = 0
        for j in range(1, i):
            if i % j == 0:
                sums += j
        if i == sums:
            print(i)


# 10. 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def boll_height(n):
    height = 100
    course = 100
    for i in range(n):
        height /= 2
        course += course + height * 2
    return height, course


# 13. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def completely():
    for i in range(100000):
        j = int(math.sqrt(i + 100))
        if i + 100 == j ** 2:
            j = int(math.sqrt(i + 100 + 168))
            if i + 168 + 100 == j ** 2:
                print(i)


# 14. 输入某年某月某日，判断这一天是这一年的第几天？(闰年： 西元年份除以400余数为0的，或者除以4为余数0且除以100不为余数0的，为
# 闰年。)
def days(year, month, day):
    day_list = [0, 31, 59, 90, 120, 151, 182, 213, 243, 273, 304, 334]
    day_num = day_list[month - 1] + day
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100) != 0):
        if month > 2:
            day_num += 1
    return day_num


# 15. 输入三个整数x，y，z，请把这三个数由小到大输出。
def sort_three(nums):
    nums = nums.split(',')
    new_nums = list()
    for num in nums:
        new_nums.append(int(num))
    new_nums.sort()
    print(new_nums)


# 16. 输出9*9口诀
def take_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {}'.format(j, i, i * j), end='\t')
        print()


# 19. 打印出如下图案（菱形）
def diamond():
    for i in range(1, 5):
        for j in range(5 - i, 1, -1):
            print(' ', end='')
        for k in range(0, (i - 1) * 2):
            print('x', end='')
        print('x')

    for i in range(1, 4):
        for j in range(0, i):
            print(' ', end='')
        for k in range(4, (i - 1) * 2, -1):
            print('x', end='')
        print('x')


# 20. 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
# 分母 前两项相加 第一项是1
def den(i):
    if i <= 1:
        return 1
    return den(i - 1) + den(i - 2)


# 分子 前两项相加 第一项是2
def mol(i):
    if i <= 0:
        return 1
    return mol(i - 1) + mol(i - 2)


# 计算前n项和
def sequence(n):
    nums = 0
    for i in range(1, n + 1):
        nums += Decimal(mol(i)) / Decimal(den(i))
    return nums


# 21. 求1+2!+3!+…+20!的和。
def sum_factorial(n):
    sums = 0
    for i in range(1, n + 1):
        sums += factorial(i)
        print(i)
    return sums


# 22. 利用递归方法求5!
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


# 53. 请根据 BMI 公式，根据用户输入计算 BMI 指数，并输出测试结果
# weight kg
# height m
# <= 18 过轻
# (18, 25] 正常
# (25, 28] 过重
# (28, 32] 肥胖
# > 32 严重肥胖
def cal_bmi(weight, height):
    bmi = Decimal(weight) // Decimal(height) ** 2
    print(bmi)
    if bmi <= 18:
        print('过轻')
    elif (bmi > 18) and (bmi <= 25):
        print('正常')
    elif (bmi > 25) and (bmi <= 28):
        print('过重')
    elif (bmi > 28) and (bmi <= 32):
        print('肥胖')
    else:
        print('严重肥胖')


if __name__ == '__main__':
    perfect_num()
    # print(boll_height(10))
    # diamond()
    # completely()
    # year = int(input('请输入年'))
    # mouth = int(input('请输入月'))
    # day = int(input('请输入日'))
    # print(days(year, mouth, day))

    # nums = input('请输入三个整数,并以逗号隔开')
    # sort_three(nums)

    # print(factorial(5))

    # weight = input('请输入体重（kg）')
    # height = input('请输入身高（m）')
    # cal_bmi(weight, height)

    # print(sum_factorial(20))

    # print(sequence(20))
