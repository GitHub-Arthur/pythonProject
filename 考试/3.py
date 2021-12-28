# -- coding: utf-8 --
# 传感器采集数据
# 传感器采集数据文件 sensor-data.txt 的一部分：
# 2018-02-28 01:03:16 19.3024 38.4629 45.08 2.68742
# 2018-02-28 01:06:16 19.1652 38.8039 46.08 2.68742
# 2018-02-28 01:06:46 19.175 38.8379 47.08 2.69964
# 其中，每行是一个读数，空格分隔多个含义，分别包括日期、时间、温度、湿度、光照和电压。其中，光照处于第 5 列。 请编写程序，统计并输出传感器采集数据中光照部分的最大值、最小值和平均值，所有值保留小数点后 2 位。‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬
# 示例1：
# 输入：无
# 输出："最大值、最小值、平均值分别是：49.08,40.08,44.37"
data = []

class chuanganqi:
    def __init__(self, date, time, shidu, wendu, guangzhao, dianya):
        self.date = date
        self.time = time
        self.shidu = shidu
        self.wendu = wendu
        self.guangzhao = guangzhao
        self.dianya = dianya


with open("sensor-data.txt", "r") as f:
    line = f.readline()
    while line != '':
        lines = line.rstrip().split(' ')
        values = chuanganqi(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
        data.append(values)
        line = f.readline()

print(max(i.guangzhao for i in data))
print(min(i.guangzhao for i in data))
average = sum(float(i.guangzhao) for i in data) / len(data)
print("%.2f" % average)
