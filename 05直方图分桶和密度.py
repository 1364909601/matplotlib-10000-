%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
# 简易直方图
data = np.random.rand(1000)
plt.hist(data);
# 设置调节参数
plt.hist(data, bins=30, density=True, alpha=0.5, 
         histtype='stepfilled', color='steelblue', edgecolor='none');
# 联合使用histtype='stepfilled'和alpha参数设置透明度在对不同分布的数据集进行比较展示时很有用
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

# 设置kwargs作为hist()函数中的参数值

kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)

# 使用**kwargs将字典中的数值传入hist()函数中
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs);
"""
如果你只是需要计算直方图的数值（即每个桶的数据点数量）而不是展示图像，np.histogram()函数可以完成这个目标：
counts, bin_edges = np.histogram(data, bins=5)
print(counts)
"""

# 二维直方图和分桶
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

# plt.hist2d : 二维直方图
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin');

# plt.hist有np.histogram, plt.hist2d有np.histsgram2d
counts, xedges, yedges = np.histogram2d(x, y, bins=30)

# plt.hexbin：六角形分桶
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')
"""
plt.hexbin有许多有趣的参数，
包括能对每个点设置权重和将每个桶的输出数据结果改为任意的 NumPy 聚合结果（带权重的平均值，带权重的标准差等）
"""


# 核密度估计KDE

from scipy.stats import gaussian_kde
# 产生和处理数据，初始化KDE
data = np.vstack([x, y])
kde = gaussian_kde(data)

# 在通用的网格中计算得到z的值
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid_
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# 将图表绘制成一张图像
plt.imshow(Z.reshape(Xgrid.shape),
           origin='lower', aspect='auto',
           extent=[-3.5, 3.5, -6, 6],
           cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")




