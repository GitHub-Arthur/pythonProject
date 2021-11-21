# 实现一个学生管理系统（用函数实现以下每个功能，用类描述学生）：
# 要求有以下功能：
# 1、添加学生(添加5个先)
# 2、删除学生（根据学号删除）
# 3、查找学生（根据学号查询，显示该学生的所有信息）
# 4、修改学生（根据学生姓名找到该学生进行信息修改，学号和班级）
# 5、查看所有学生
# 6、退出
# 每个学生的信息包括：姓名  学号   班级
import os


# 学生类
class Student:
    def __init__(self, name, number, group):
        self.name = name
        self.number = number
        self.group = group

    def __str__(self):
        return str(self.name) + "\t" + str(self.number) + "\t" + str(self.group)

    """
    笔记:
    __str__（）这个特殊方法会在尝试将对象转换为字符串的时候调用
    它的作用可以用来指定对象转换为字符串的结果  （print函数）
    """


# 学生管理系统类
class StudentManager(Student):
    students = []

    # 1、添加学生
    @classmethod
    def addStudent(cls):
        name = input("please input name:")
        number = input("please input number:")
        group = input("please input group:")
        student = Student(name, number, group)
        cls.students.append(student)
        cls.write()

    # 2、删除学生（根据学号删除）
    @classmethod
    def delete(cls):
        number = input("please input the number what you want delete:")
        for student in cls.students:
            if student.number == str(number):
                cls.students.remove(student)
                cls.write()
                break
        else:
            print("there is not have the student")

    # 3、查找学生（根据学号查询，显示该学生的所有信息）
    @classmethod
    def search(cls):
        number = input("please input the number what you want search:")
        for student in cls.students:
            if student.number == str(number):
                print("Name\tNumber\tGroup")
                print(student)
                break
        else:
            print("there is not have the student")

    # 4、修改学生（根据学生姓名找到该学生进行信息修改，学号和班级）
    @classmethod
    def update(cls):
        name = input("please input the name what you want update")
        for student in cls.students:
            if student.name == name:
                index = cls.students.index(student)
                cls.students[index].number = str(input("Please input your new number:"))
                cls.students[index].group = str(input("Please input your new group:"))
                cls.write()
                return  # 考虑到学生有同名的情况
        else:
            print("there is not have the student")

    """
    笔记:
    python String index（）函数返回找到指定子字符串的最低索引。 如果未找到子字符串，则引发ValueError 。
    """

    # 5、查看所有学生
    @classmethod
    def display(cls):
        print("Name\tNumber\tGroup")
        for student in cls.students:
            print(student)

    # 将学生数据存储到student.dat
    @classmethod
    def write(cls):
        with open("student.dat", "w") as f:
            for student in cls.students:
                f.write(student.name + "," + str(student.number) + "," + str(student.group) + "\n")

    # 初始化从student.dat读取已经有的学生数据
    @classmethod
    def read(cls):
        a = os.path.exists('student.dat')
        if a:
            with open("student.dat", "r") as f:
                line = f.readline()
                while line != '':
                    lines = line.rstrip().split(',')
                    student = Student(lines[0], lines[1], lines[2])
                    cls.students.append(student)
                    line = f.readline()
        else:
            print("file open error")

    # 学生管理系统菜单
    @staticmethod
    def menu():
        print("*" * 30)
        print("1:add")
        print("2:delete")
        print("3:search")
        print("4:update")
        print("5:display")
        print("6:exit")
        print("*" * 30)

    # 学生管理系统运行
    @staticmethod
    def run():
        StudentManager.read()
        while True:
            StudentManager.menu()
            operator = input("please input your choice:")
            if operator == "1":
                StudentManager.addStudent()
            if operator == "2":
                StudentManager.delete()
            if operator == "3":
                StudentManager.search()
            if operator == "4":
                StudentManager.update()
            if operator == "5":
                StudentManager.display()
            if operator == "6":
                print("成功退出学生管理系统")
                break


if __name__ == "__main__":
    StudentManager.run()
