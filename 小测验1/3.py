# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字
# 再将第一位和第四位交换，第二位和第三位交换。试输入一个数，并求出对应的数字
# 方法一/二选其一运行
# 方法一
a = int(input('输入四个数字:'))
b = [a % 10, a % 100 // 10, a % 1000 // 100, a // 1000]  # 个十百千
for i in range(4):
    b[i] += 5
    b[i] %= 10
for i in range(2):
    b[i], b[3 - i] = b[3 - i], b[i]
for i in range(3, -1, -1):
    print(str(b[i]), end="")

# 方法二
# a = int(input('输入四个数字:'))
# b = [a % 10, a % 100 // 10, a % 1000 // 100, a // 1000] # 个十百千
#
# for i in range(4):
#     b[i] += 5
#     b[i] %= 10
# for i in range(4):
#     print(str(b[i]), end="")
# 1、4交换，2、3交换其实就是倒序输出
