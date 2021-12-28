# 【实例】小学生计算器。利用函数实现能够求100以内的加减法、10以内的乘除法。
import random


def compute():
    op = random.choice('+-*/')
    if op == '*':
        op1 = random.randint(0, 10)
        op2 = random.randint(0, 10)
        result = op1 * op2
    elif op == '/':
        op2 = random.randint(0, 10)
        m = random.randint(0, 10)
        op1 = op2 * m
        result = op1 / op2
    else:
        op1 = random.randint(0, 100)
        op2 = random.randint(0, 100)
        result = op1 + op2
        if op == '-':
            if op1 < op2:
                op1, op2 = op2, op1
            result = op1 - op2
    print(op1, op, op2, '=', end='')
    return result


count = 0
for i in range(10):
    answer = compute()
    yAnswer = int(input())
    if yAnswer == answer:
        count = count + 10
print("your score is :", count)
