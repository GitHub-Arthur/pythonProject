# 【实例】猜数字。
# 本案例的任务：系统随机生成一个1.100之间的整数，然后让用户猜测该数字，如果用户猜的数据比答案大，提示太大了，如果小，则提示太小了， 正确则输出用户猜测正确。
# 案例分析：根据案例需要实现的功能，可以将任务分解为两个子任务：产生数字和用户猜数字，并用两个函数实现。
import random


def main():
    # 1.系统生成一个随机数并放到number中。
    number = newNumber()
    # 2.让用户猜测number的值到底是几。
    guessNumber(number)


def newNumber():
    number = random.randint(1, 101)
    return number


def guessNumber(number):
    yAnswer = int(input("enter a integer between 0-100:"))
    if yAnswer > number:
        print("too big")
    elif yAnswer < number:
        print("too small")
    else:
        print("right")


if __name__ == '__main__':
    main()
