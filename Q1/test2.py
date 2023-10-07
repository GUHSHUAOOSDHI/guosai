import numpy as np
import matplotlib.pyplot as plt
# 创建一个空的251x251矩阵
matrix = np.zeros((251, 251))

# 对角线元素赋值为1
np.fill_diagonal(matrix, 1)

# 生成-1到1之间的随机数，并填充到矩阵的上半部分
upper_triangle = np.random.uniform(-1, 1, (251, 251))
upper_triangle = np.triu(upper_triangle, 1)
matrix += upper_triangle

# 使用矩阵的上半部分来填充下半部分，以满足对称性
matrix = matrix + matrix.T

# 创建一个下半部分的掩码
mask = np.tri(251, 251, k=-1)

# 将上半部分的值设为NaN
data = np.where(mask, matrix, np.nan)
# 绘制热力图

plt.imshow(data, cmap='coolwarm')
plt.colorbar()  # 添加颜色条
plt.title('Spearman Correlation Heatmap')
plt.show()