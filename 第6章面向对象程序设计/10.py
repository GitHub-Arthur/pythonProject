'''
我们有一个汽车参数接口，里面定义了汽车所有的必须需要的参数，然后由本田汽车的类，奥迪汽车的类，大众汽车的类，
他们都实现了汽车接口，这样就好办了，大家选择汽车的时候，只需要将不同汽车的参数来进行对比，就能评判出一个车的好坏。
'''

import abc


# 抽象类：本质还是类，与普通类额外的特点的是：加了装饰器的函数，子类必须实现他们
class Car(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def name(self):  # 如果子类没有name 函数，主动抛出异常
        '必须定义车名字'
        pass

    @abc.abstractmethod
    def Model(self):  # 如果子类没有Model 函数，主动抛出异常
        '必须定义车型号'
        pass

    @abc.abstractmethod
    def drive(self):
        ' 必须定义驱动方式 '
        pass

    @abc.abstractmethod
    def Fuel(self):
        '必须定义油耗'
        pass

    @abc.abstractmethod
    def engine(self):
        '必须定义发动机'
        pass

    @abc.abstractmethod
    def power(self):
        '必须定义功率'
        pass


class AudiCar(Car):
    name = '一汽-大众奥迪-奥迪Q5L'

    def Model(self):
        print('中型SUV')

    def drive(self):
        print('前置四驱7挡双离合')

    def Fuel(self):
        print('7.1L/100km(工信部)')

    def engine(self):
        print('2.0T 190马力 L4')

    def power(self):
        print('140kW/320N.m')


class BMWCar(Car):
    name = '宝马'

    def Model(self):
        print('中型SUV')

    def drive(self):
        print('前置四驱7挡双离合')

    def Fuel(self):
        print('5.1L/100km(工信部)')

    def engine(self):
        print('3.0T 190马力 L4')

    def power(self):
        print('1990kW/320N.m')


Audi = AudiCar()
BMW = BMWCar()
