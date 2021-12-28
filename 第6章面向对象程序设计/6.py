# 五、派生类
# 1. 在父类的基础上产生子类，产生的子类就叫做派生类
# 2. 父类里没有的方法，在子类中有了，这样的方法就叫做派生方法。
# 3. 父类里有，子类也有的方法，就叫做方法的重写（就是把父类里的方法重写了)
class Hero:
    def __init__(self, nickname, aggressivity, life_value):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):
        print('Hero attack')


class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):  # self=g1,enemy=r1
        # self.attack(enemy) #g1.attack(r1)，这里相当于无限递归
        Hero.attack(self, enemy)  # 引用 父类的 attack，对象会去跑 父类的 attack
        print('from garen attack')  # 再回来这里

    def fire(self):
        print('%s is firing' % self.nickname)


class Riven(Hero):
    camp = 'Noxus'


g1 = Garen('garen', 18, 200)
r1 = Riven('rivren', 18, 200)
g1.attack(r1)
print(g1.camp)
print(r1.camp)
g1.fire()
