# 输入一个正整数n，计算 1!+2!+3!+...+n! 的和并输出
n = int(input())
tmp = 1
count = 0
i = 1
while n >= i:
    tmp = tmp * i
    count = count + tmp
    i = i + 1
print(count)
