# 1定义一个学生类：成员属性包括 姓名（私有）、年龄（私有）
# 成绩（语文，数学，英语)（私有）
# 1、成员方法：
#   a、获取学生的姓名
#   b、获取学生的年龄
#   c、显示该学生的姓名 年龄，成绩
#   d、返回3门科目中最高的分数
# 2、设置一个静态方法：
#   e、返回当前产生的学生对象数量

#学生类
class Student:
    count = 0

    def __init__(self, name, age, cou):
        self.__name = name
        self.__age = age
        self.__course = cou
        Student.count += 1

    # 获取学生的姓名
    def get_name(self):
        print('学生的姓名是', self.__name)

    # 获取学生的年龄
    def get_age(self):
        print('学生的年龄是', self.__age, '岁')

    # 显示该学生的姓名 年龄，成绩
    def show_list(self):
        self.get_name()
        self.get_age()
        for key, value in self.__course.items():
            print(key + "的成绩为", value, "分")

    # 返回3门科目中最高的分数
    def get_course(self):
        print('该学生分数最高的科目是', max(self.__course, key=self.__course.get), '\n分数为',
              self.__course[max(self.__course, key=self.__course.get)], '分')

        '''
        笔记：
        python的max()函数解决
        获取字典中value最大的值对应的key ：max(self.__course, key=self.__course.get)
        获取字典中value最大值 : self.__course[max(self.__course, key=self.__course.get)]
        '''

    # 返回当前产生的学生对象数量
    @staticmethod
    def students_number():
        print('现在总共有', Student.count, '位学生')


cjy = Student('Chen Jiongyu', 20, {'语文': 70, '数学': 100, '英语': 80})
cjy.get_name()
cjy.get_age()
cjy.show_list()
cjy.get_course()
cjy.students_number()
