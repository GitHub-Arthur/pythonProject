# 【实例】猜数字
# 目前guessNumber函数中对于猜对猜错仅仅给出提示信息
# 没有返回任何值给调用它的函数guessTime，这样无法控制何时退出循环体
# 考虑修改guessNumber函数
# 如果猜对，除了输出提示信息外，还返回1
# 如果猜错，提示太大或者太小，并且返回0
# 这样可以在guessTimes中根据guessNumber的返回值来判断是否退出循环。
import random


def main():
    number = newNumber()
    times = 10
    guessTime(number, times)


def newNumber():
    number = random.randint(1, 101)
    return number


def guessNumber(number):
    yAnswer = int(input("enter a integer between 0-100:"))
    if yAnswer > number:
        print("too big")
        return 0
    elif yAnswer < number:
        print("too small")
        return 0
    else:
        print("right")
        return 1


def guessTime(number, times):
    for i in range(times):
        if guessNumber(number) == 1:
            print("你一共猜了", i + 1, "次")
            break
    if i > times:
        print("sorry,你没有猜对，正确答案是", number)


if __name__ == '__main__':
    main()
