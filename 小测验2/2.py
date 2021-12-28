# -- coding: utf-8 --
# 2、数列求和
# 描述
# 用户输入一个小于10的正整数，求1 + 12 + 123 + 1234 + ……的前n项的和输入
# 一个正整数n（测试数据保证小于10）
# 输出    数列的和
#
# 输入输出示例
#
# 输入
# 5
# 输出
# 13715


def SUM(n):
    s = 0
    i = 1
    s += i
    while i % 10 < int(n):
        i = i * 10 + i % 10 + 1
        s += i
    return s


n = eval(input("请输入一个正整数n(n<10):"))
while n >= 10:
    n = eval(input("n的范围错误,请重新输入:"))
print(SUM(n))
