# 【实例】猜数字。
# 程序只给了用户一次机会，现在考虑给用户10次机会
# 因此程序中增加了一个函数guessTimes(number)
# 该函数用一个循环来调用guessNumber(number)函数，循环次数为10。
import random


def main():
    # 1.系统生成一个随机数并放到number中。
    number = newNumber()
    # 2.让用户猜测number的值到底是几。
    guessTime(number)


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


def guessTime(number):
    for i in range(10):
        guessNumber(number)


if __name__ == '__main__':
    main()
