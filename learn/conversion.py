import json

# list tuple dict set str 之间的相互转化
names_list = ['Tom', 'Jerry', 'Jack', 'Marry']
names_tuple = ('Tom', 'Jerry', 'Jack', 'Marry')
names_dict = {'Tom': 'to', 'Jerry': 'do', 'Jack': 'every', 'Marry': 'list'}
names_set = {'Tom', 'Jerry', 'Jack', 'Marry'}

# list转
# str
# 拼接为字符串
print(''.join(names_list))

# tuple
print(tuple(names_list))

# dict
# 使用fromkeys来构造一个值固定的字典
print({}.fromkeys(names_list, 'do'))
# 使用两个list，一个做键一个做值 使用了zip函数
keys = names_list
values = ['to', 'do', 'every', 'list']
print(dict(zip(keys, values)))

# set
print(set(names_list))


# tuple转
# str
# 拼接字符串
print(''.join(names_tuple))

# list
print(list(names_tuple))

# dict
# 使用fromkeys来构造一个值固定的字典
print({}.fromkeys(names_tuple, 'do'))
# 使用两个tuple，一个做键一个做值 使用了zip函数
keys = names_tuple
values = ('to', 'do', 'every', 'list')
print(dict(zip(keys, values)))

# set
print(set(names_tuple))


# dict转
# str
# 键转
print(''.join(names_dict))
# 值转
print(''.join(names_dict.values()))

# list
print(list(names_dict))
print(list(names_dict.values()))

# tuple
print(tuple(names_dict))
print(tuple(names_dict.values()))

# set
print(set(names_dict))
print(set(names_dict.values()))


# set转
# str
print(''.join(names_set))

# list
print(list(names_set))

# tuple
print(tuple(names_set))

# dict
# 使用fromkeys来构造一个值固定的字典
print({}.fromkeys(names_set, 'do'))
# 使用两个set，一个做键一个做值 使用了zip函数
keys = names_set
values = {'to', 'do', 'every', 'list'}
print(dict(zip(keys, values)))


# str转
# list
str_list = "['Tom', 'Jerry', 'Jack', 'Marry']"
print(eval(str_list))

# tuple
str_tuple = "{'Tom', 'Jerry', 'Jack', 'Marry'}"
print(eval(str_tuple))

# dict
# 使用eval
str_dict = "{'Tom': 'to', 'Jerry': 'do', 'Jack': 'every', 'Marry': 'list'}"
print(eval(str_dict))
# 使用json 注：使用json里面必须是双引号"" 这是json的格式要求
str_dict = '{"Tom": "to", "Jerry": "do", "Jack": "every", "Marry": "list"}'
print(json.loads(str_dict))

# set
str_set = "{'Tom', 'Jerry', 'Jack', 'Marry'}"
print(eval(str_set))
