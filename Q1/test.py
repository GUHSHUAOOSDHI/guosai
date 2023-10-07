import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from sklearn.preprocessing import MinMaxScaler

# 示例数据
DanDict1 = {'花叶类': 41546.11599999995, '花菜类': 7815.231000000082, '水生根茎类': 4794.958999999989, '茄类': 5862.958000000013, '辣椒类': 22913.315000000308, '食用菌': 14466.955000000005}
DanDict2 = {'花叶类': 55171.796000000104, '花菜类': 11890.340000000011, '水生根茎类': 8445.68600000003, '茄类': 8204.904999999972, '辣椒类': 21963.592000000124, '食用菌': 13720.533}
DanDict3 = {'花叶类': 52868.353000000105, '花菜类': 11375.210000000061, '水生根茎类': 12291.234000000055, '茄类': 3854.516999999997, '辣椒类': 20847.27400000011, '食用菌': 21753.308999999976}
DanDict4 = {'花叶类': 48934.71300000001, '花菜类': 10685.670000000046, '水生根茎类': 15049.474000000058, '茄类': 4509.402000000027, '辣椒类': 25864.44800000005, '食用菌': 26145.927999999996}
labels = ['花叶类', '花菜类', '水生根茎类', '茄类', '辣椒类', '食用菌']
x1 = list(DanDict1.values())
x2 = list(DanDict2.values())
x3 = list(DanDict3.values())
x4 = list(DanDict4.values())

data = np.empty((4, 6))

data[0] = x1
data[1] = x2
data[2] = x3
data[3] = x4
# 创建MinMaxScaler对象
scaler = MinMaxScaler()

# 对矩阵进行归一化
data = scaler.fit_transform(data)
print(data)

# 计算斯皮尔曼相关系数
corr_matrix, _ = spearmanr(data)

# 绘制热力图
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
# 设置坐标轴刻度
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xticks(np.arange(len(labels)), labels)
plt.yticks(np.arange(len(labels)), labels)
plt.title('Pearson Correlation Heatmap')
plt.show()