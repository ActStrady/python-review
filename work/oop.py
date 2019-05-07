

# 1. 定义类，实现 power(x, n) 功能
# 2. 定义类，实现字符串逆序
class Solution:
    @staticmethod
    def power(num, power_num):
        return num ** power_num

    @staticmethod
    def reverse_words(string):
        return string[::-1]


# 3. 定义三角形类，实现求三角形周长和面积的方法，属性为三个边长
class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def are(self):
        p = (self.__a + self.__b + self.__c) / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

    def perimeter(self):
        return self.__a + self.__b + self.__c


# 4. 定义立方体类，属性为长度、宽度、高度，通过方法来计算它的体积
class Cube:
    def __init__(self, long, wide, high):
        self.__long = long
        self.__wide = wide
        self.__high = high

    def volume(self):
        return self.__long * self.__wide * self.__high


# 5. 定义一个人类，包含姓名、性别、年龄等信息
# 所有的变量必须私有。其他类只能通过该类的方法获取和修改
# 实例化一个人类，试着通过该类的方法修改实例化的人的信息
class People:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def __str__(self):
        return 'People object name={}, sex={}, age={}'.format(self.__name, self.__sex, self.__age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# 6. 定义一个学生类，包含三个属性（学号，姓名，成绩）均为私有的
# 分别给这三个属性定义两个方法，一个设置它的值，另一个获得它的值
# 测试这些方法
class Student:
    def __init__(self, sid, name, score):
        self.__sid = sid
        self.__name = name
        self.__score = score

    def __str__(self):
        return 'Student object sid={}, name={}, score={}'.format(self.__sid, self.__name, self.__score)

    def get_sid(self):
        return self.__sid

    def set_sid(self, sid):
        self.__sid = sid

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


# 7. 继承人类编写一个学生类，为学生类添加新的属性和方法，并进行测试
class GoodStudent(People):
    def __init__(self, sid, name, sex, age, score):
        super().__init__(name, sex, age)
        self.__sid = sid
        self.__score = score

    def __str__(self):
        return 'GoodStudent object sid={}, name={}, sex={}, age={}, score={}' \
            .format(self.__sid, self.get_name(), self.get_sex(), self.get_age(), self.__score)

    def get_sid(self):
        return self.__sid

    def set_sid(self, sid):
        self.__sid = sid

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


if __name__ == '__main__':
    print(Solution.power(2, -3))
    print(Solution.power(3, 5))
    print(Solution.power(100, 0))

    print(Solution.reverse_words('hello.py'))

    print(Triangle(3, 4, 5).are())
    print(Triangle(3, 4, 5).perimeter())

    print(Cube(4, 5, 6).volume())

    tom = People('Tom', '女', 25)
    tom.set_name('Jerry')
    tom.set_sex('男')
    tom.set_age(12)
    print(tom)

    hua = Student('18504120101', '张华', 85)
    hua.set_sid('18714251685')
    hua.set_name('张化')
    hua.set_score(95)
    print(hua.get_sid())
    print(hua.get_name())
    print(hua.get_score())
    print(hua)

    mark = GoodStudent('185012515658', '刘强', '男', 16, 100)
    print(mark)
