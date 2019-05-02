## python重点
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