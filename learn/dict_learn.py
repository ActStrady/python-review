import collections
# dict特点：键值对、无序、可修改
# 何时使用：需要键值对

# 定义
people = {'Tony': 'Iron Man', 'Steven': 'Captain'}
# 构造
people1 = dict(Tony='Iron Man', Steven='Captain')
# 使用列表或元组
people2 = {}.fromkeys(('Tony', 'Steven'))
# 可以有一个值，只能是一个
people3 = {}.fromkeys(['Tony', 'Steven'], 'Iron Man')
print(people)
print(people1)
print(people2)
print(people3)

# 加
people['Ban'] = 'Hok'

# 取
print(people['Steven'])
# 使用get方法来取 找不到会返回None 也可以指定一个新的值
print(people.get('Toy'))
print(people.get('Sr', 'null'))

# 改
people2['Tony'] = 'Stark'
# update方法 当没有这个值的时候会新增一个
people3.update(Toy='tons')
people3.update({'Tony': 'Steven'})
print(people2)
print(people3)

# 删
del people['Tony']
# 删除指定
people2.pop('Steven')
# 删除最后一个
people3.popitem()
print(people)
print(people2)
print(people3)

# 长度
print(len(people))

# 拷贝
print(people.copy())

# 迭代
# 键
for name in people.keys():
    print(name)
# 值
for role in people.values():
    print(role)
# 键值
for name, role in people.items():
    print(name, role)

# collections 的 OrderedDict是有序的字典，顺序就是插入的顺序
print('----------OrderedDict---------------')
people = collections.OrderedDict(people)
for name, role in people.items():
    print(name, role)

# 清空
people1.clear()
print(people1)

# 利用内置函数删除掉本身
# del people
# del people1
# del people2
# del people3

# 小练习
# 6. 把 3 个 dict 合并为 1 个 dict
print('---------练习------------')
print(people)
print(people2)
print(people3)
people.update(people2)
people.update(people3)
print(people)

# 7. 把一个 dict 按 key 排序输出
print(people)
names = list()
for name in people.keys():
    names.append(name)
names.sort()
for name in names:
    print(name, people[name])

# 8. 找出两个 dict 中的 key-value 相同项
print('--------------------')
print(people)
print(people3)
print('--------------------')
for name1, role1 in people.items():
    for name2, role2 in people3.items():
        if (name1 == name2) and (role1 == role2):
            print(name1, role1)
