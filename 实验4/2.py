# 编写一函数Prime(n)，对于已知正整数n，判断该数是否为素数，如果是素数，返回True,否则返回False。
from math import sqrt

def Prime(n):
    s = 0
    tag = True
    if n > 0:
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i) == 0:
                s += 1
    if s >= 1:
        tag = False
    return tag


primes = []
for i in range(1, 101):
    if Prime(i):
        primes.append(i)

print(primes)
