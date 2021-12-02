# -- coding: utf-8 --
# 1、设计一个函数，生成指定长度为6位数的验证码，验证码由数字和大小写英文字母构成的随机字符串。

import random


def yanzhengma():
    length = 6
    x = 0
    while x < length:
        s = random.choice(range(1, 4))
        if s == 1:
            a = random.choice(range(1, 10))
            print(a, end='')
            x += 1
        if s == 2:
            b = random.choice(range(65, 90))
            print(chr(b), end='')
            x += 1
        if s == 3:
            c = random.choice(range(97, 122))
            print(chr(c), end='')
            x += 1


yanzhengma()
