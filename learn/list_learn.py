# 首先明确list的特点：可重复、有序、任意类型、可修改
# 何时使用：存可变可重复的有序数据

# 常用的方法
# 定义
names = ['Jerry', 'Tom', 'Tony']

# 构造器 可以传一个元组
nums = list((1, 2, 3, 4))
print(nums)

# 取
print(names[-1])

# 元素是否存在
print('Tom' in names)

# 加
names.append('Tim')
print(names)

# 插入
names.insert(1, 'Fun')
print(names)

# 删
names.remove('Fun')
print(names)

# 根据下标删元素 没参数默认删除尾元素
names.pop()
print(names)

# 改
names[0] = 'State'
print(names)

# 长度
print(len(names))

# 返回索引 可以有开始和结束的参数
print(names.index('Tom'))

# 统计数量
print(names.count('Tom'))

# 拷贝
names1 = names.copy()
print(names1)

# 扩展
names.extend(names1)
print(names)

# 逆序
names.reverse()
print(names)

# 排序 key参数是排序函数 reverse默认是false
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# 迭代
for name in names:
    print(name)

# 清空
names.clear()
print(names)
names1.clear()
print(names1)

# 利用内置函数删除掉本身
del names
del names1

# 小练习
# 1. 求一个数值 list 的所有元素和
nums = [1, 2, 3, 6, 7, 9, 5, 7, 55]
num_sum = 0
for num in nums:
    num_sum += int(num)
print(num_sum)

# 2. 求一个数值 list 的最大/最小元素值
print("max:{}, min:{}".format(max(nums), min(nums)))

# 3. 求一个字符串 list 中，字符串长度大于2，且首尾字符相同的元素个数
strings = ['a', 'xy', 'alabama', '101', '三弟三']
count = 0
for string in strings:
    if (len(string) > 2) and (string[0] == string[-1]):
        print(string)
        count += 1
print(count)
