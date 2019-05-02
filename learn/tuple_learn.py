# 明确tuple的特点：可重复、有序、任意类型、不可修改
# 何时使用：可以使用的时候尽量使用，安全考虑

# 常用方法
# 定义
names = ('Jerry', 'Tom', 'Tony')
# 特别注意的是：当只有一个元素时也必须添加,
names1 = ('Jerry',)

# 构造器 可以传一个列表
nums = tuple([1, 2, 3, 4])
print(nums)

# 取
print(names[-1])

# 元素是否存在
print('Tom' in names)

# 长度
print(len(names))

# 返回索引 可以有开始和结束的参数
print(names.index('Tom'))

# 统计数量
print(names.count('Tom'))

# 长度
print(len(nums))
print(len(names))

# 迭代
for name in names:
    print(name)

# 利用内置函数删除掉本身
del names
del names1

# 小练习
# 4. 把 一个 tuple 转为字符串
print("".join(names))

# 5. 对一个 tuple 进行各种切片操作
# 倒序
print(names[::-1])

# 切片0-1
print(names[0:1])

# 相当于复制
print(names[::])

