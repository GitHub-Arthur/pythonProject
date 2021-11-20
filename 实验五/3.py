# 实现一个学生管理系统（用函数实现以下每个功能，用类描述学生）：
# 要求有以下功能：
# 1、添加学生(添加5个先)
# 2、删除学生（根据学号删除）
# 3、查找学生（根据学号查询，显示该学生的所有信息）
# 4、修改学生（根据学生姓名找到该学生进行信息修改，学号和班级）
# 5、查看所有学生
# 6、退出
# 每个学生的信息包括：姓名  学号   班级

# 学生类
class Student:
    count = 0

    def __init__(self, name, number, group):
        self.__name = name
        self.__number = number
        self.__group = group
        Student.count += 1






# cjy = pupil('Chen Jiongyu', 20, {'语文': 70, '数学': 100, '英语': 80}, '物联网1901班')
# cjy.show_list()
