# 切片
sentence = 'jack Can i help you?'
# 前六个字符
print(sentence[0:6])
# 每隔两个取一个
print(sentence[0:6:2])
# 把字符串反过来
print(sentence[::-1])

# 忽略转义r或R
print(r'\t')

# 格式化输出
print('%d, %s' % (4, 'nu'))

# format
print('the words is {}, and {}'.format('new', 'news'))

# 首字母变成大写,其他字符变为小写
print(sentence.capitalize())

# 前后使用规定字符填充，使目标字符串居中
print(sentence.center(30, '-'))

# 前面使用0填充，填充到指定的长度
print(sentence.zfill(30))

# 字符出现的次数，还可以指定前后的位置
print(sentence.count('a'))
print(sentence.count('a', 0, 3))

# 是否以xx开头和结尾, 可以指定起始
print(sentence.startswith('j', 1, 5))
print(sentence.endswith('?', 0, 10))

# 找到指定字符在字符串中最初出现的位置，可以指定起始,返回-1表示没有找到
print(sentence.find('i'))
print(sentence.find('i', 1, 8))

# 指定字符串里tab的长度
s = 'news\tnew'
print(s.expandtabs(4))
print(s.expandtabs(8))

# 判定是否是字母或者数字组成
s = 'Jack25'
print(s.isalnum())
print(sentence.isalnum())

# 判定是否只由字母组成
s = 'Jack'
print(s.isalpha())
print(sentence.isalpha())

# 判定字母是否都是小写
s = 'jack11'
print(s.islower())
print(sentence.islower())

# 判定字母是否都是大写
s = 'JACK11'
print(s.isupper())
print(sentence.isupper())

'''
    digit 含义时数字 位数字 
    numeric 含义时数字
    decimal 含义是十进制
    isdigit() isnumeric() isdecimal() 的区别
    1. isdigit可以判定阿拉伯数字和byte数字
              不可判定罗马数字和汉字数字
    2. isnumeric可以判定阿拉伯数字和汉字以及罗马数字
                但没有判定byte数字的方法
    3. isdecimal可以判定阿拉伯数字
                不可以判定罗马数字和汉字数字
'''
# 判定是否数字组成
s = '125'
print(s.isnumeric())
print(sentence.isnumeric())

# 判定是否数字组成
s = '185'
print(s.isdigit())
print(sentence.isdigit())

# 判定是否数字组成
s = '211'
print(s.isdecimal())
print(sentence.isdecimal())

# 判定是否是只包含空格的字符串
s = '       '
print(s.isspace())
print(sentence.isspace())

# 字符串来连接指定序列 join里的是序列
print(sentence.join('adc'))

# 字母都变小写
print(sentence.lower())

# 字母都变大写
print(sentence.upper())

# 大写变小写，小写变大写
print(sentence.swapcase())

# 去初字符串两端、左端、右端指定的字符，默认去除空格、换行符、tab
s = '  \t  ssd   \n   '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = '-.-- ssd - ,--'
print(s.strip('- .,'))
print(s.lstrip('- .,'))
print(s.rstrip('- ,.'))

# 取出字符串里ascII码最大最小的字符
print(max(sentence))
print(min(sentence))

# 替换 可以指定最多替换几次
s = 'news and peoples and fuck'
print(s.replace(' ', '-'))
print(s.replace(' ', '-', 3))
