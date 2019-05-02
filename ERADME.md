## python重点
- list tuple dict set str 之间的相互转化
    - 一般来说都是构造函数的使用
    - 以下是一些特殊的用法汇集
        1. list tuple dict set 拼接为字符串：`''.join()`
        2. list tuple set 转换为字典可以使用
            1. `{}.fromkeys()`来构造一个不同键相同值的字典
            2. `zip()`来将两个list或tuple或set构造为字典
        3. str 转 list tuple dict set
            1. 主要使用`eval()`只要把字符串改为对应的格式就可以动态的转化为对应的结构
            2. 转dict还有另外一种方式`json.loads()`,需要注意的是必须严格的使用json格式：键和值都用双引号`""`包裹 