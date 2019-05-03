# 1. 读取一个文本文件的前 N 行
def read_line(path, num, mode):
    lines = list()
    with open(path, mode, encoding='utf-8') as f:
        for i in range(num):
            line = f.readline().strip()
            lines.append(line)
    return lines


# 2. 按行读取一个文件，把每行内容存入一个 list
def line_list(path, mode):
    lines = list()
    with open(path, mode, encoding='utf-8') as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines


# 3. 查询一篇英文文章的最长单词
def long_word(path):
    # 单词列表
    words = list()
    # 最长单词列表
    long_words = list()
    # 单词和单词长度字典
    word_and_len = dict()

    # 读取文章并分割
    with open(path, encoding='utf-8') as f:
        # split() 函数不加参数表示以换行和空格等符号分割
        strings = f.read().split()
    # 处理单词 去掉各种标点
    for string in strings:
        word = string.strip(',.?!'':[]""')
        words.append(word)
    # 添加单词和其长度
    for word in words:
        word_and_len[word] = len(word)
    # 找到最长的单词
    for word, count in word_and_len.items():
        if count == max(word_and_len.values()):
            long_words.append(word)
    return long_words


# 4. 找出一片英文文章的最高频单词
def high_word(path):
    # 单词列表
    words = list()
    # 高频词列表
    high_words = list()

    # 读取文章并分割
    with open(path, encoding='utf-8') as f:
        strings = f.read().split()
    # 处理单词 去掉各种标点
    for string in strings:
        word = string.strip(',.?!'':[]""')
        words.append(word)
    # 初始化单词字典
    word_and_nums = {}.fromkeys(words, 0)
    # 统计单词出现的频率
    for word in words:
        for i in word_and_nums.keys():
            if i == word:
                word_and_nums[i] += 1
    # 找出频率最高的单词
    for word, count in word_and_nums.items():
        if count == max(word_and_nums.values()):
            high_words.append(word)
    return high_words


if __name__ == '__main__':
    print(read_line('str.py', 5, 'rt'))
    print(line_list('news.txt', 'rt'))
    print(long_word('news.txt'))
    print(high_word('news.txt'))
