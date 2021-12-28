"""
类的组合，即在类实例化时，将另一个类的实例作为参数传入，这样可以将两个实例关联起来。
当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合比较好。
比如学生类和课程类,学生需要选课,可以选一门或者多门,在没选课之前,学生类和课程类无关
当类之间有很多相同的属性，提取这些统统的属性做成基类，用继承比较好。

"""


# 学校类 是学生类和老师类的父类
class School:
    schoolName = '学习训练营'

    def __init__(self, name, sex, age, birth):
        self.name = name
        self.sex = sex
        self.age = age
        self.birth = birth  # 类的组合 ，将生日在初始化的时候就被调用


# 学生类
class students(School):

    def __init__(self, name, sex, age, id, birth):
        School.__init__(self, name, sex, age, birth)
        self.id = id
        self.course = []

    def Learn(self):
        print('%s,正在学习' % self.name)


# 老师类
class teacher(School):

    def __init__(self, name, sex, age, level, birth):
        School.__init__(self, name, sex, age, birth)
        self.id = id
        self.level = level
        self.course = []

    def Teach(self):
        print('%s,正在上课' % self.name)


# 课程类 是学生和老师的组合类
class Course:
    def __init__(self, name, price, cycle):
        self.name = name
        self.price = price
        self.cycle = cycle

    def all_info(self):
        print('课程信息：%s---%s---%s' % (self.name, self.price, self.cycle))


# 生日类，是学生类和老师类的组合类
class date:
    def __init__(self, year, month, day):
        self.year = year
        self.mouth = month
        self.day = day

    def birthday(self):
        print('出生日期为：%s-%s-%s' % (self.year, self.mouth, self.day))


# 学生
birth = date('2000', 12, 19)
stu1 = students('jasn', 'male', 18, '002', birth)
stu1.Learn()
stu1.birth.birthday()

# 老师
birth = date('1993', 12, 23)  # 定义生日对象
python = Course('python', 13000, '3mon')  # 定义课程对象
linux = Course('linux', 13000, '3mon')

teach1 = teacher('nancy', 'male', 18, 10, birth)
teach1.Teach()
teach1.birth.birthday()
teach1.course.append(python)  # 将课程添加到老师中，这也是一种组合关系

# 查看课程
for course in teach1.course:
    course.all_info()
