# 设计一个函数，要求对字典{5：“five”，2:”two”，3：“three”，1：“one”}中的键按照有小到大的顺序，一次输出每个键的值
def my_sort(dic):
    for key, value in sorted(dic.items(), key=lambda x: x[0]):
        print(value)


dict1 = {5: "five", 2: "two", 3: "three", 1: "one"}
my_sort(dict1)
