# 类似其他语言的三目运算符
print('new' if 's' is '2' else 'old')

# range()函数，配合循环使用，用来限制循环次数
for i in range(10):
    print(i, end='')

# 循环后加else 当循环没有被break的时候执行else的内容
s = 'new is old'
for char in s:
    if char == 'x':
        print('有x')
        break
else:
    print('没有x')
# 一个使用 else的实例：找出101 - 200 的所有素数
counter = 0
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        counter += 1
print(counter)
# 不使用else
counter = 0
flag = True
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
        flag = True
    if flag:
        print(i)
        counter += 1
print(counter)
