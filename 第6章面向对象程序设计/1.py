# 【实例】编写程序，输入圆的半径，输出圆的面积和周长
import math


# Circle类的定义
class Circle:
    # __init__方法是一个特殊的方法：构造方法
    # 当创建对象时，系统自动调用__init__方法，它没有返回值
    # 一般都在构造方法中初始化实例属性
    def __init__(self, r):
        self.__radius = r

    # area、perimeter是普通的实例方法,是圆类对外的接口
    # 通过对象名.方法名(参数列表)来调用
    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


r1 = float(input("请输入圆的半径："))
c1 = Circle(r1)
print(c1.area())
print(c1.perimeter())
