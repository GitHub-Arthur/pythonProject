# 【实例】现在养狗的人越来越多
# 狗的主人都会给自己的狗起一个名字，每一条狗都有年龄，每一条狗都会跑，会叫。
# 设计一个狗类，完成对狗的抽象和封装
# 类Dog
class Dog:
    def __init__(self, name, age):
        self.__name = name  # 私有成员name的初始化
        self.__age = age  # 私有成员age的初始化

    def run(self):
        print(self.__name + " is running")
        print("It is " + str(self.__age) + " old years")

    def bark(self):
        print(self.__name + " is barking:汪汪，汪汪...")


# 测试代码
dog1 = Dog("黄豆", 4)  # 创建一个对象dog1
dog1.run()  # 在类外调用公有成员方法run
dog1.bark()  # 在类外调用公有成员方法bark

