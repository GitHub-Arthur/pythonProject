# 【实例】利用函数实现将2~20之间的所有素数
import math


def prime(num):  # 判断m是否是素数，是返回1，不是返回0
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return 0
        i = i + 1
    return 1


print("2~20之间的素数有：")
for m in range(2, 20):
    if prime(m) == 1:
        print(m, " ", end='')
