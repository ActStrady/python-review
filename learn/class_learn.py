# 开闭原则， 对扩展开放，对修改关闭，意思是增加新功能，来扩展代码，而不是修改已有代码，和设计模式相关

# 多继承
# TODO super()函数的使用和mro顺序

# TODO 装饰器的使用 eg：@property @staticmethod等

# 定制类 TODO 定制类的其他一些 如__iter__ 以及元类以及枚举类等
import types


# 类定义，类名后小括号的内容表示继承，基类也是object,可省略
class People(object):
    # 定义允许自由绑定的属性名，注意：光在父类写，在子类不起作用，要起作用的话，在子类也定义__slots__,这时子类的范围为子类+父类
    __slots__ = ('sex', 'name', '__age')

    # 强制定义属性
    def __init__(self, name, age):
        self.name = name
        # 私有
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


class Student(People):
    # self:类本身 类里的方法必须带self
    # 在子类也定义__slots__, 这时子类的范围为子类 + 父类
    __slots__ = ('_kw', 'get_name', 'id')

    def __init__(self, name, age, **kw):
        super().__init__(name, age)
        # 保护
        self._kw = kw

    def walk(self):
        print(self.name, self.get_age(), 'walk')

    # 类似于java的toString
    def __str__(self):
        return 'Student object:(name={}, age={}, {})'.format(self.name, self.get_age(), self._kw)


# 所谓鸭子类型就是只关注行为不关注类型
class Duck(object):
    """
    鸭子类，有walk方法，这样就可以传入某一方法，实现类似多态
    """

    @staticmethod
    def walk():
        print('Duck walk')


# 类似多态的实现
# 动态语言多态通过鸭子类型来实现
def fn_walk(student):
    student.walk()


# 获取对象信息相关方法
# isinstance 判定对象是否是该类型，包括继承关系
tom = Student('Tom', 20, gender='男', married=True)
print(isinstance(2, int))
print(isinstance(tom, People))
print(isinstance(tom, Student))

# type 获取对象类型
print(type(23))
print(type('s'))
print(type(abs))
print(type(tom))

# types 内置很多类型的一个类型常量集
print(types.FunctionType)
print(types.BuiltinFunctionType)

# dir 获取对象的属性和方法
print(dir(tom))
print(tom.__class__)
print(dir('a'))
print('a'.__len__())

# hasattr getattr setattr 对象获取其属性和方法，反射的思想
# 是否有
print(hasattr(tom, 'name'))
# 获取 第三个参数表示获取不到返回的默认值
print(getattr(tom, 'name'))
# 设置
setattr(tom, 'name', 'marry')
print(getattr(tom, 'name', 'user'))


# 定制类
# 特殊方法/魔术方法
# __slots__ 限制实例的属性


def get_name(self):
    return self.name


# 使用MethodType为实例动态绑定函数
tom.get_name = types.MethodType(get_name, tom)
print(tom.get_name())
# 为类添加一个方法，相当于增加一个类属性
Student.get_name = get_name

# __str__ 打印实例的方法
print(tom)

if __name__ == '__main__':
    # 自由绑定属性
    tom.id = '02454'
    print(tom.id)

    # 鸭子类型实现类似多态
    fn_walk(tom)
    duck = Duck
    fn_walk(duck)
