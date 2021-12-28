# -- coding: utf-8 --
# 用户登录
#
# 描述
# 有字典如下：
# dic = {'admin': '123456', 'administrator': '12345678', 'root': 'password'}
#
# 实现用户输入用户名和密码，当用户名与密码和字典中的键值对匹配时，显示“登录成功”，
# 否则显示“登录失败”，登录失败时允许重复输入三次。
#
# 输入格式:
# 在两行中分别输入用户名和密码
#
# 输出格式:
# "登录成功"或"登录失败"

dic = {'admin': '123456', 'administrator': '12345678', 'root': 'password'}

timer = 0  # 循环次数

while timer < 3:
    name = input("用户名:")
    password = input("密码:")
    n = 0
    for key, value in dic.items():
        if key == name and value == password:
            break
        else:
            n += 1
    if n < 3:
        print("登录成功")
        break
    else:
        print("登录失败")
        timer += 1
