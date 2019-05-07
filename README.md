## python学习与深入理解
#### python 和其他语言不一样的地方
- 没有equals方法，有 is 关键字
- 没有三目运算符 有 `condition_is_true if condition else condition_is_false`
- print函数会换行，要让其不换行，要使用print函数的 `end=''` 该参数表示打印的末尾加什么,可以是任何
- 循环后加else 当循环没有被break的时候执行else的内容
- 一种for循环的特殊写法`[i for i in range(10)]`，这样直接返回的是一个列表
- python函数也是对象，所以函数也可以被用来赋值，你可以把函数赋值给一个简单的名
- 函数不写内容可以写个 `pass`表示空函数
- python的函数文档注释是写在函数里面最开始的
- 可以返回多参数，实际上是被封装为一个元组
- python是动态语言，所以类的属性在__init__函数定义，故在类里定义的属性是类属性，相当于其他语言的静态属性
---
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
---
#### str 的几个重要方法
- 反转字符串 `str[::-1]`
- 首字母大写 `capitalize()`
- 使用指定字符居中填充 `center(size, char)`
- 前面使用0填充，填充到指定的长度 `zfill(size)`
- 指定字符串里tab的长度 `expandtabs()`
- 字符串来连接指定序列 `join()`
---
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
---
#### 文件读写
- `decode()`方法表示解码使用的字符集，多用在解码网络爬取的数据
- 给定路径的指定文件列表`[x for x in os.listdir('.') if os.path.isfile(os.path.join('.', x)) and os.path.splitext(x)[1] == '
.py']` 本实例是当前路径下所有py的文件列表
- 给定路径的指定文件夹列表`[x for x in os.listdir('../') if os.path.isdir(os.path.join('../', x))]` 本实例是上级目录的所有文件夹列表
---
#### 函数及函数式编程
- 函数的异常处理: `raise` 抛出异常
- 函数也可以用来赋值，函数文档注释写在函数内最开始，可以返回多参数，实际是返回一个元组
- 内置函数*TODO [内置函数](https://docs.python.org/zh-cn/3/library/functions.html)*
---
#### OOP
- 类定义，类名后小括号的内容表示继承，基类是object可省略
- 属性
    - 自由绑定属性，可以在调用的时候直接给定义属性和赋值
    - 强制定义属性， 在__init__作为参数
    - 类属性，定义在类里，类的所有实例都可以使用
- 权限
    - __开头表示私有，
    - _表示保护，一般用在模块，from import * 引用不到
    - __开头和结尾的表示一些内置（魔法）的属性和函数
- 多态
    - 动态语言多态通过鸭子类型来实现,所谓鸭子类型就是只关注行为不关注类型
- 开闭原则， 对扩展开放，对修改关闭，意思是增加新功能，来扩展代码，而不是修改已有代码，和设计模式相关
- 多继承
    - *TODO super()函数的使用和mro顺序*
- 获取对象信息
    - type获对象类型
    - types有很多常见的类型
    - isinstance判定对象是否是该类型，包括继承关系
    - dir获取对象的属性和方法
    - hasattr getattr setattr 对象操作其属性和方法，也就反射的思想
- 语法糖，装饰器的使用 *TODO 装饰器的使用 eg：@property等*
- 定制类：对类进行定制，使用特殊方法/魔术方法
    - `__slots__` 限制实例的属性 光在父类写，在子类不起作用，要起作用的话，在子类也定义__slots__,这时子类的范围为子类+父类
    - `__str__` 打印对象时调用的方法，类似java的tostring
    - MethodType为实例动态绑定函数
    - *TODO 其他的定制方法以及元类和枚举类*
