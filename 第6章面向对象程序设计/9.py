# 九、抽象类和归一化设计
# 接口提取了一群类共同的函数，可以把接口当做一个函数的集合。然后让子类去实现接口中的函数。
# 这么做的意义在于归一化，什么叫归一化，就是只要是基于同一个接口实现的类，
# 那么所有的这些类产生的对象在使用时，从用法上来说都一样。
# 归一化的好处：
# 1、归一化让使用者无需关心对象的类是什么，只需要的知道这些对象都具备某些功能就可以了，这极大地降低了使用者的使用难度。
# 2、归一化使得高层的外部使用者可以不加区分的处理所有接口兼容的对象集合

class Interface:  # 定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
    def read(self):  # 定接口函数read
        pass

    def write(self):  # 定义接口函数write
        pass


class Txt(Interface):  # 文本，具体实现read和write
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')


class Sata(Interface):  # 磁盘，具体实现read和write
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')


class Process(Interface):
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')
