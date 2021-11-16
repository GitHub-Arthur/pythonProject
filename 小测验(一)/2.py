# 判断一个列表是否存在重复元素，如果存在，则全部输出
# 同时，输出重复个数最多的元素（注：要考虑到存在数量相同的元素情况）

hash_table = {}
nums = [0, 0, 1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9]
for i in nums:
    hash_table[i] = 1 + hash_table.get(i, 0)
print(hash_table)
max_count = 0
print("重复的元素有")
for key, value in hash_table.items():
    if value != 1:
        print(key, end=" ")
        if value > max_count: max_count = value
print("\n重复出现最多次数的元素是")
for key, value in hash_table.items():
    if value == max_count:
        print(key, end=" ")
