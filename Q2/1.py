# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_excel(r".\1.xlsx")
data2 = pd.read_excel(r".\2.xlsx")
keys1 = data1["分类名称"].tolist()
keys2 = data1["单品编码"].tolist()

LeiDict = {key: 0.0 for key in keys1}
print(LeiDict)
#品类销量字典

MaLeiDict =dict(zip(data1["单品编码"], data1["分类名称"]))
#编码对应品类
x1=[]
y1=[]


k=0
b = data2["销售日期"][0].strftime('%Y-%m-%d %H:%M:%S')
x1.append(0.0)
y1.append(0.0)
for i in range(len(data2["销售日期"])):
    a = data2["销售日期"][i].strftime('%Y-%m-%d %H:%M:%S')
    if MaLeiDict[data2["单品编码"][i]] == '花叶类':
        if a!=b:
            x1.append(data2["销量(千克)"][i])
            y1.append(data2["销售单价(元/千克)"][i] * data2["销量(千克)"][i])
            k += 1
            b=a
        else:
            x1[k] += data2["销量(千克)"][i]
            y1[k] += data2["销售单价(元/千克)"][i] * data2["销量(千克)"][i]

print(x1)
print(y1)