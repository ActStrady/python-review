# 特点：无序、不重复、可修改
# 何时使用：存不重复的元素时

# 定义 可以是元组不可是列表和字典也不可是集合
names = {'Jerry', 'Tom', 'Tony', 'Jerry', 'Tom', 'Tony', ()}
print(names)

# 加
names.add(('age', 'name'))
print(names)

# 删
# 指定删
names.remove('Tom')
print(names)
# 随机删
names.pop()
print(names)

# 迭代
for name in names:
    print(name)

# 拷贝
print(names.copy())

# 集合的各种运算 每种计算都有update后缀的方法，代表直接把集合更新为操作后的
names1 = {'Jerry', 'Tom', 'Tony'}
print('names1', names1)
names2 = {'Jerry', 'Tim', 'Tony', 'Mark'}
print('names2', names2)
# 差集 表示集合剪掉和其一样的值
print('差集', names1.difference(names2))
# 交集
print('交集', names1.intersection(names2))
# 是否不存在交集 有交集则返回False
print('是否不存在交集', names1.isdisjoint(names2))
# 是否子集
print('是否子集', names1.issubset(names2))
# 是否超集
print('是否超集', names1.issuperset(names2))
# 对称差集 就是除去交集的其他的
print('对称差集', names1.symmetric_difference(names2))
# 并集
print('并集', names1.union(names2))
# 更新为并集 ，这个和上边比比较特殊
# names1.update(names2)
print('更新为并集', names1)

# & |
# & 与交集一样
print(names1 & names2)
# | 与并集一样
print(names1 | names2)

# 清理
names.clear()
names1.clear()
names2.clear()

# 删除
del names
del names1
del names2

# 小练习
# 9. 求一个 set 的最大/最小元素值
nums = {1, 5, 6, 8, 9, 57}
print('最大', max(nums))
print('最小', min(nums))

# 10. 把两个 set 中的不同元素构造为一个新的 set 并输出
nums1 = {1, 5, 6, 8, 9, 57}
nums2 = {2, 5, 8, 58, 558}
nums3 = nums1.symmetric_difference(nums2)
print(nums3)

