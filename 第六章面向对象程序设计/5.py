class animal:  # 定义父类
    country = 'china'  # 这个叫类的变量

    def __init__(self, name, age):
        self.name = name  # 这些又叫数据属性
        self.age = age

    def walk(self):  # 类的函数，方法，动态属性
        print('%s is walking' % self.name)

    def say(self):
        pass


class people(animal):  # 子类继承父类
    pass


class pig(animal):  # 子类继承父类
    pass


class dog(animal):  # 子类继承父类
    pass


haha = people('haha', 60)  # 实例化一个对象
print(haha.name)
haha.walk()
