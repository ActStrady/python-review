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

# 4. 把 一个 tuple 转为字符串
names = ('Jerry', 'Tom', 'Tony')
print("".join(names))

# 5. 对一个 tuple 进行各种切片操作
# 倒序
print(names[::-1])

# 切片0-1
print(names[0:1])

# 相当于复制
print(names[::])

# 6. 把 3 个 dict 合并为 1 个 dict
people = {'Tony': 'Iron Man', 'Steven': 'Captain'}
# 构造
people1 = dict(Tony='Iron Man', Steven='Captain')
# 使用列表或元组
people2 = {}.fromkeys(('Tony', 'Steven'))
# 可以有一个值，只能是一个
people3 = {}.fromkeys(['Tony', 'Steven'], 'Iron Man')
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

# 9. 求一个 set 的最大/最小元素值
nums = {1, 5, 6, 8, 9, 57}
print('最大', max(nums))
print('最小', min(nums))

# 10. 把两个 set 中的不同元素构造为一个新的 set 并输出
nums1 = {1, 5, 6, 8, 9, 57}
nums2 = {2, 5, 8, 58, 558}
nums3 = nums1.symmetric_difference(nums2)
print(nums3)
