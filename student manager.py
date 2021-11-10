# 添加学生信息(例如添加5个)
# 注：每个学生的信息包括：姓名、学号、班级即可
# 2、删除学生（根据学号删除）
# 3、查找学生（例如根据学号查询，显示该学生的所有信息）
# 4、修改学生（例如根据学生姓名找到该学生，修改其学号或班级信息）
# 5、显示所有学生信息
# 6、退出

print("=" * 46)
print("学生管理系统".center(40))
print("输入1：表示添加学生".center(40))
print("输入2：表示删除学生".center(40))
print("输入3：表示查找学生".center(40))
print("输入4：表示修改学生".center(40))
print("输入5：表示查看所有学生".center(40))
print("输入6：表示退出".center(40))
print("=" * 46)
student = []

while True:
    id = input("请输入你想要的操作")
    if id == "1":
        stu = {}
        name = input("请输入想姓名")
        number = input("请输入学号")
        classroom = input("请输入班级")
        stu["name"] = name
        stu["number"] = number
        stu["classroom"] = classroom
        student.append(stu)
        print("添加成功")
    elif id == "2":
        number = input("请输入你要删除的学生的学号（如果不知道学号，请先查看全部人,序号-1）")
        if number == "-1":
            print("序号\t姓名\t学号\t班级")
            for count, i in enumerate(student, 1):
                print("%s\t\t%s\t\t%s\t\t%s\t" % (count, i["name"], i["number"], i["classroom"]))
            continue
        else:
            student.remove(student[int(number)-1])
            print("删除成功")
    elif id == "3":
        number = input("请输入你要查找同学的学号")
        for stud in student:
            if stud["number"] == number:
                print("姓名\t学号\t班级")
                print("%s\t\t%s\t\t%s\t" % (stud["name"], stud["number"], stud["classroom"]))
                break
        else:  # 注意  for     else
            print("你查找的%s不存在" % number)
    elif id == "4":
        name = input("请输入你要修改同学的姓名")
        for stud in student:
            if stud["name"] == name:
                iaa = input("请输入修改的信息编号【1.姓名 2.学号 3.班级】")
                if iaa == "1":
                    name = input("请输入姓名")
                    stud["name"] = name
                elif iaa == "2":
                    number = input("请输入学号")
                    stud["number"] = number
                elif iaa == "3":
                    classroom = input("请输入班级")
                    stud["classroom"] = classroom
                print("修改成功")
                break
    elif id == "5":
        print("序号\t姓名\t学号\t班级")
        for count, i in enumerate(student, 1):
            print("%s\t\t%s\t\t%s\t\t%s\t" % (count, i["name"], i["number"], i["classroom"]))
    elif id == "6":
        print("退出")
        break
