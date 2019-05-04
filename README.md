## python重点
#### python 和其他语言不一样的地方
- 没有equals方法，有 is 关键字
- 没有三目运算符 有 `condition_is_true if condition else condition_is_false`
- print函数会换行，要让其不换行，要使用print函数的 `end=''` 该参数表示打印的末尾加什么,可以是任何
- 循环后加else 当循环没有被break的时候执行else的内容
- 一种for循环的特殊写法`[i for i in range(10)]`，这样直接返回的是一个列表
#### Anaconda3命令
- 常用的命令
    1. 更新库：`conda upgrade --all`
    2. 查看虚拟环境列表：`conda env list`
    3. 创建虚拟环境： `conda create -n name python=2 or 3`
    4. 进入虚拟环境： `activate name`
        1. 安装包： `conda install package-name`
        2. 卸载包： `conda remove package-name`
        3. 更新包： `conda update package_name`
        3. 查看包列表： `conda list`
        4. 导出虚拟环境： `conda env export > path/name.yaml`
    5. 退出虚拟环境： `deactivate name`
    6. 删除虚拟环境： `conda remove -n name --all`
    7. 导入虚拟环境： `conda create -f path/name.yaml`
#### str 的几个重要方法
- 反转字符串 `str[::-1]`
- 首字母大写 `capitalize()`
- 使用指定字符居中填充 `center(size, char)`
- 前面使用0填充，填充到指定的长度 `zfill(size)`
- 指定字符串里tab的长度 `expandtabs()`
- 字符串来连接指定序列 `join()`
#### list、tuple、dict、set、str之间的相互转化
- 一般来说都是构造函数的使用
- 以下是一些特殊的用法汇集
    1. list tuple dict set 拼接为字符串：`''.join()`
    2. list tuple set 转换为字典可以使用
        1. `{}.fromkeys()`来构造一个不同键相同值的字典
        2. `zip()`来将两个list或tuple或set构造为字典
    3. str 转 list tuple dict set
        1. 主要使用`eval()`只要把字符串改为对应的格式就可以动态的转化为对应的结构
        2. 转dict还有另外一种方式`json.loads()`,需要注意的是必须严格的使用json格式：键和值都用双引号`""`包裹
#### Python 文件读写
- `decode()`方法表示解码使用的字符集，多用在解码网络爬取的数据
- 给定路径的指定文件列表`[x for x in os.listdir('.') if os.path.isfile(os.path.join('.', x)) and os.path.splitext(x)[1] == '
.py']` 本实例是当前路径下所有py的文件列表
- 给定路径的指定文件夹列表`[x for x in os.listdir('../') if os.path.isdir(os.path.join('../', x))]` 本实例是上级目录的所有文件夹列表

