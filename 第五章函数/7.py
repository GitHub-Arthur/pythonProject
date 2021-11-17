# 分析：我国目前将垃圾分为四种类型：
# 可回收垃圾、厨余垃圾、有害垃圾和其他垃圾。
# 用列表变量将每种类型的常见垃圾罗列出来，
# 定义三个全局列表变量用来存储可回收垃圾、厨余垃圾、有害垃圾，其他的不在这三个列表中的就都属于其他垃圾。
# 系统首先根据用户输入的垃圾名称判断属于四种垃圾中的哪一类，然后执行对应的操作。
# 垃圾分类
waste_recycle = ["paper", "glasses", "bottle", "plastic"]  # 可回收垃圾：
waste_kitchen = ["peel", "vegetable", "leftover", "flower"]  # 厨余垃圾
waste_harmful = ["battery", "light tube", "daily chemical"]  # 有害垃圾


def handle_harmful():
    print("This is harmful waste and please put it into the red trash can ")


def handle_kitchen():
    print("This is kitchen waste and please put it into the green trash can ")


def handle_recycle():
    print("This is recycle waste and please put it into the blue trash can ")


def handle_others():
    print("This is other waste and please put it into the yellow trash can ")


def do_with_waste(waste):
    if waste in waste_harmful:
        handle_harmful()
    elif waste in waste_kitchen:
        handle_kitchen()
    elif waste in waste_recycle:
        handle_recycle()
    else:
        handle_others()


waste = input("enter waste name:")
do_with_waste(waste)
