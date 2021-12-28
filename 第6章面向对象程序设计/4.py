
# python中子类继承父类成员变量之间的取值逻辑

class Person():

    def __init__(self, name, age, sex):
        self.name = "jasn"
        self.age = '18'
        self.sex = sex

    def talk(self):
        print("i want to speak something to yo!!")


class Chinese(Person):
    def __init__(self, name, age, sex, language):
        Person.__init__(self, name, age, sex)  # 用父类的name,age，sex 覆盖掉子类的属性
        self.age = age  # 覆盖掉了父类的age,取值为子类实例中传入age参数
        self.language = "chinese"

    def talk(self):
        print("我说的是普通话！！")
        Person.talk(self)


obj = Chinese("nancy",'20','male',"普通话")

print(obj.name)  # 对应场景A
print(obj.age)  # 对应场景B
print(obj.language)  # 对应场景C
obj.talk()  # 对应场景D

# 总结：
# A:若父类中初始化了成员变量，子类调用父类构造方法未覆盖属性（self.name），则调用子类属性时取值为父类中初始化的成员变量；
# B:若父类中初始化了成员变量，若子类调用父类构造方法覆盖属性（self.age）则取值为子类实例中传入参数
# C:若父类未初始化该成员变量，则无论子类中有无进行对父类构造方法进行属性的覆盖，均取子类实例中传入的参数
# D:对于方法,如果子类有这个方法则直接调用，如果子类没有则去父类查找。父类没有则报错

