# 【实例】如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1**3 + 5**3 + 3**3，因此 153 就是一个水仙花数。利用函数求1000以内的水仙花数（3位数）。
def Narcissistic(num):
    a = num // 100
    b = (num - a * 100) // 10
    c = (num - a * 100 - b * 10)
    if num == pow(a, 3) + pow(b, 3) + pow(c, 3):
        return 1
    else:
        return 0


print("三位数的水仙花数有：")
for i in range(100, 1000):
    if Narcissistic(i) == 1:
        print(i)
