# -*- coding: UTF-8 -*-
import pandas as pd

data1 = pd.read_excel(r".\2 - 副本.xlsx")
data2 = pd.read_excel(r".\3 - 副本.xlsx")
data3 = pd.read_excel(r".\5.xlsx")
LiRun = {}
sold1 = {}
sold2 = {}
sold3 = {}
sold4 = {}
sold5 = {}
sold6 = {}
sold7 = {}


for i in range(len(data1["销售单价(元/千克)"])):
    a = data1["销售日期"][i].strftime('%Y-%m-%d %H:%M:%S')
    if data1["单品编码"][i] in LiRun:
        LiRun[data1["单品编码"][i]] += data1["销售单价(元/千克)"][i] * data1["销量(千克)"][i]
        if a[8:10] == "24":
            if data1["单品编码"][i] in sold1:
                sold1[data1["单品编码"][i]] += data1["销量(千克)"][i]
            else:
                sold1[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "25":
            if data1["单品编码"][i] in sold2:
                sold2[data1["单品编码"][i]] += data1["销量(千克)"][i]
            else:
                sold2[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "26":
            if data1["单品编码"][i] in sold3:
                sold3[data1["单品编码"][i]] += data1["销量(千克)"][i]
            else:
                sold3[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "27":
            if data1["单品编码"][i] in sold4:
                sold4[data1["单品编码"][i]] += data1["销量(千克)"][i]
            else:
                sold4[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "28":
            if data1["单品编码"][i] in sold5:
                sold5[data1["单品编码"][i]] += data1["销量(千克)"][i]
            else:
                sold5[data1["单品编码"][i]] = data1["销量(千克)"][i]
        if a[8:10] == "29":
            if data1["单品编码"][i] in sold6:
                sold6[data1["单品编码"][i]] += data1["销量(千克)"][i]
            else:
                sold6[data1["单品编码"][i]] = data1["销量(千克)"][i]
        else:
            if data1["单品编码"][i] in sold7:
                sold7[data1["单品编码"][i]] += data1["销量(千克)"][i]
            else:
                sold7[data1["单品编码"][i]] = data1["销量(千克)"][i]
    else:
        LiRun[data1["单品编码"][i]] = data1["销售单价(元/千克)"][i] * data1["销量(千克)"][i]
        if a[8:10] == "24":
            sold1[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "25":
            sold2[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "26":
            sold3[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "27":
            sold4[data1["单品编码"][i]] = data1["销量(千克)"][i]
        elif a[8:10] == "28":
            sold5[data1["单品编码"][i]] = data1["销量(千克)"][i]
        if a[8:10] == "29":
            sold6[data1["单品编码"][i]] = data1["销量(千克)"][i]
        else:
            sold7[data1["单品编码"][i]] = data1["销量(千克)"][i]

sunhao = {}
print(data3)
for i in range(len(data3["单品编码"])):
    sunhao[data3["单品编码"][i]] = data3["损耗率(%)"][i]

for key, value in sold1.items():
    if value <= 2.5 * (1-sunhao[key]):
        sold1[key] = 2.5
    else:
        sold1[key] = value / (1-sunhao[key])

for key, value in sold2.items():
    if value <= 2.5 * (1-sunhao[key]):
        sold2[key] = 2.5
    else:
        sold2[key] = value / (1-sunhao[key])

for key, value in sold3.items():
    if value <= 2.5 * (1-sunhao[key]):
        sold3[key] = 2.5
    else:
        sold3[key] = value / (1-sunhao[key])

for key, value in sold4.items():
    if value <= 2.5 * (1-sunhao[key]):
        sold4[key] = 2.5
    else:
        sold4[key] = value / (1-sunhao[key])

for key, value in sold5.items():
    if value <= 2.5 * (1-sunhao[key]):
        sold5[key] = 2.5
    else:
        sold5[key] = value / (1-sunhao[key])

for key, value in sold6.items():
    if value <= 2.5 * (1-sunhao[key]):
        sold6[key] = 2.5
    else:
        sold6[key] = value / (1-sunhao[key])

for key, value in sold7.items():
    if value <= 2.5 * (1-sunhao[key]):
        sold7[key] = 2.5
    else:
        sold7[key] = value / (1-sunhao[key])

for i in range(len(data2["日期"])):
    a = data2["日期"][i].strftime('%Y-%m-%d %H:%M:%S')
    if data2["单品编码"][i] in LiRun:
        if a[8:10] == "24":
            if data2["单品编码"][i] in sold1:
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * sold1[data2["单品编码"][i]]
            else:
                max_value = float('-inf')
                for dictionary in [sold1, sold2, sold3, sold4, sold5, sold6, sold7]:
                    if data2["单品编码"][i] in dictionary:
                        value = dictionary[data2["单品编码"][i]]
                        if value > max_value:
                            max_value = value
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * max_value
        elif a[8:10] == "25":
            if data2["单品编码"][i] in sold2:
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * sold2[data2["单品编码"][i]]
            else:
                max_value = float('-inf')
                for dictionary in [sold1, sold2, sold3, sold4, sold5, sold6, sold7]:
                    if data2["单品编码"][i] in dictionary:
                        value = dictionary[data2["单品编码"][i]]
                        if value > max_value:
                            max_value = value
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * max_value
        elif a[8:10] == "26":
            if data2["单品编码"][i] in sold3:
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * sold3[data2["单品编码"][i]]
            else:
                max_value = float('-inf')
                for dictionary in [sold1, sold2, sold3, sold4, sold5, sold6, sold7]:
                    if data2["单品编码"][i] in dictionary:
                        value = dictionary[data2["单品编码"][i]]
                        if value > max_value:
                            max_value = value
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * max_value
        elif a[8:10] == "27":
            if data2["单品编码"][i] in sold4:
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * sold4[data2["单品编码"][i]]
            else:
                max_value = float('-inf')
                for dictionary in [sold1, sold2, sold3, sold4, sold5, sold6, sold7]:
                    if data2["单品编码"][i] in dictionary:
                        value = dictionary[data2["单品编码"][i]]
                        if value > max_value:
                            max_value = value
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * max_value
        elif a[8:10] == "28":
            if data2["单品编码"][i] in sold5:
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * sold5[data2["单品编码"][i]]
            else:
                max_value = float('-inf')
                for dictionary in [sold1, sold2, sold3, sold4, sold5, sold6, sold7]:
                    if data2["单品编码"][i] in dictionary:
                        value = dictionary[data2["单品编码"][i]]
                        if value > max_value:
                            max_value = value
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * max_value
        if a[8:10] == "29":
            if data2["单品编码"][i] in sold6:
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * sold6[data2["单品编码"][i]]
            else:
                max_value = float('-inf')
                for dictionary in [sold1, sold2, sold3, sold4, sold5, sold6, sold7]:
                    if data2["单品编码"][i] in dictionary:
                        value = dictionary[data2["单品编码"][i]]
                        if value > max_value:
                            max_value = value
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * max_value
        else:
            if data2["单品编码"][i] in sold7:
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * sold7[data2["单品编码"][i]]
            else:
                max_value = float('-inf')
                for dictionary in [sold1, sold2, sold3, sold4, sold5, sold6, sold7]:
                    if data2["单品编码"][i] in dictionary:
                        value = dictionary[data2["单品编码"][i]]
                        if value > max_value:
                            max_value = value
                LiRun[data2["单品编码"][i]] -= data2["批发价格(元/千克)"][i] * max_value

print(LiRun)

sorted_dict = sorted(LiRun.items(), key=lambda x: x[1])
print(sorted_dict)

