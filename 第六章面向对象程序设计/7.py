"""
当类是新式类，多继承的情况下，在要查找的属性不存在时，会按照广度优先来查找
默认从左侧分支查找，如 ：class G(D,E,F):会先从 D 的分支查找 找到 D-C 然后从E-B -F 顺序查找
最后再查找 几个类所共同继承的顶级父类，如果顶级没有，则报错
"""


class A:
    def test(self):
        print('A中的test')

    pass


class B(A):
    def test(self):
        print('B中的test')

    pass


class C(A):
    def test(self):
        print('C中的test')

    pass


class D(C):
    def test(self):
        print('D中的test')

    pass


class E(B):
    def test(self):
        print('E中的test')

    pass


class F(A):
    def test(self):
        print('F中的test')

    pass


class G(D, E, F):
    def test(self):
        print('G中的test')

    pass


obj = G()
obj.test()

'''
第一次 E中的test
注释D，第二次：C中的test
注释C，第三次：E中的test
注释E，第四次：B中的test
注释B，第五次，F中的test
注释F，第六次，A中的test

所以新式类的继承关系（查找顺序）为:  
obj-->G --> D-->C -->E -->B -->F -->A  
也称广度优先

'''
print(F.__mro__)  # 只有新式才有这个属性可以查看线性列表，经典类没有这个属性

# 新式类继承顺序:F->D->B->E->C->A
# 经典类继承顺序:F->D->B->A->E->C
# python3中统一都是新式类
# python2中才分新式类与经典类 class A(object) 为经典类
