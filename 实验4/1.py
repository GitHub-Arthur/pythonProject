def Fb(n):
    a, b = 1, 1
    count = 0
    while (count != n - 2):
        a, b = b, a + b
        count += 1
    return b
n = eval(input('please input n:'))
print(Fb(n))
