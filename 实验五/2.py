# 基于学生类再派生一个 小学生类
# 成员属性：班级
# 成员方法：显示该学生的姓名 年龄，成绩,班级

# 学生类
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


# 小学生类
class pupil(Student):
    # 成员属性：班级
    def __init__(self, name, age, cou, group):
        Student.__init__(self, name, age, cou)
        self.__group = group

    # 成员方法：显示该学生的姓名 年龄，成绩,班级
    def show_list(self):
        Student.show_list(self)
        print('学生的班级为', self.__group)


cjy = pupil('Chen Jiongyu', 20, {'语文': 70, '数学': 100, '英语': 80}, '物联网1901班')
cjy.show_list()
