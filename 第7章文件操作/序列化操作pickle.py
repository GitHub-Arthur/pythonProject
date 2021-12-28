# -- coding: utf-8 --
import pickle


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))


aa = Person("张三", 20)

i = 13000000
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu1 = (-5, 10, 8)
dic1 = {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange'}
with open('序列化操作pickle.dat', 'wb') as f:
    pickle.dump(5, f, 0)
    pickle.dump(i, f, 0)
    pickle.dump(list1, f, 0)
    pickle.dump(tu1, f, 0)
    pickle.dump(dic1, f, 0)
    pickle.dump(aa, f, 0)

with open('序列化操作pickle.dat', 'rb') as f:
    n = pickle.load(f)
    while n > 0:
        print(pickle.load(f))
        n -= 1
