# 1从键盘的输入包括自己的学号，姓名，年龄，班级，性别，邮箱信息，身高；
# 最后将这些变量通过格式化的方式打印在屏幕上（选用两种格式化方式打印）；
# 显示的格式例如:我的姓名是
#             我的身高xxx米
#             我的年龄xxx 等
number = int(input("学号:"))
name = input("姓名:")
age = int(input("年龄:"))
your_class = input("班级:")
sex = input("性别:")
e_mail = input("邮箱:")
height = int(input("身高:"))

print("输入格式1\n我的学号是{}\n我的姓名是{}\n我的年龄是{}岁\n我的班级是{}\n我的性别为{}\n我的邮箱地址是{}\n我的身高{}米\n".format(number, name, age, your_class,
                                                                                         sex, e_mail, height))
print(
    f"输入格式2\n我的学号是{number}\n我的姓名是{name}\n我的年龄是{age}岁\n我的班级是{your_class}\n我的性别为{sex}\n我的邮箱地址是{e_mail}\n我的身高{height}米\n")
