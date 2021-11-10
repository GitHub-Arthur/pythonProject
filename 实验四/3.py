# 求润年Leapyear(n)，输入年份，统计该年是不是润年，如果是润年，返回True；否则返回False。

def Leapyear(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return True
    else:
        return False


if Leapyear(eval(input('请输入年份：'))):
    print('该年份是闰年')
else:
    print('该年份不是闰年')
