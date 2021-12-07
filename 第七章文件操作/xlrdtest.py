# -- coding: utf-8 --
import xlrd

# 读取本地csv文件,打开excel文件（默认是rb方式打开）
# xlrd更新到了2.0版本，只支持.xls文件，不支持.xlsx文件
myWorkbook = xlrd.open_workbook('xlrdtest.xls')
mySheet = myWorkbook.sheet_by_index(0)  # 通过索引顺序获得
# 获取行数和列数
nrows = mySheet.nrows
ncols = mySheet.ncols
print("The rows: %d" % nrows)
print("The cols: %d" % ncols)
# 获取一行和一列
for i in range(nrows):
    myRowValues = mySheet.row_values(i)
    print(myRowValues)
for j in range(ncols):
    myColValues = mySheet.col_values(j)
    print(myColValues)
