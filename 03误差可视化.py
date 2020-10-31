# 在数据和结果的可视化中，有效地展示这些误差能使你的图表涵盖和提供更加完整的信息

%matplotlib inline
import matplotlib.pyplot as plt
plt.styple.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(X) + dy * np.random.randn(50)
# fmt参数控制线条和点风格的代码，与plt.plot有相同的语法
plt.errorbar(x, y, yerr=dy, fmt='.k');

# errorbar函数还有很多参数可以用来精细调节图表输出
# 使用这些参数你可以很容易的个性化调整误差条的样式
# 通常将误差线条颜色调整为浅色会更加清晰
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgry', elinewidth=3, capsize=0);

# 除了上面介绍的参数，你还可以指定水平方向的误差条（xerr），单边误差条和其他很多的参数
# 参阅plt.errorbar的帮助文档获得更多信息

# 连续误差
"""在某些情况下可能需要对连续值展示误差条。虽然Matplotlib没有内建函数能直接完成这个任务
   但是可以利用plt.plot和plt.fill_between函数结合起来达到目的。
"""
from sklearn.gaussian_process import GaussianProcessRegressor

# 定义模型和一些符合模型的点
model = lambda x: x* np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# 计算高斯过程回归，使其符合fit数据点
gp = GaussianProcessRegressor()
gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
yfit, std = gp.predict(xfit[:, np.newaxis], return_std=True)
dyfit = 2 * std     # 两倍sigma ~ 95% 确定区间
"""
我们现在有了xfit、yfit和dyfit，作为对我们数据的连续拟合值以及误差限
我们也可以像上面一样使用plt.errorbar绘制误差条
但是事实上我们不希望在图标上绘制 1000 个点的误差条
但是事实上我们不希望在图标上绘制 1000 个点的误差条
"""
# 可视化结果
plt.plot(xdata, ydata, 'or')
plt.plot(xfit, yfit, '-', color='gray')
plt.fill_between(xfit, yfit - dyfit, yfit + dyfit, color='gray', alpha=0.2)
plt.xlim(0, 10);
# fill_between函数：传递的参数包括 x 值，y 值的低限，然后是 y 值的高限
"""
上图为我们提供了一个非常直观的高斯过程回归展示：
  在观测点的附近，模型会被限制在一个很小的区域内，
  反映了这些数据的误差比较小。在远离观测点的区域，
  模型开始发散，反映了这时的数据误差比较大。
"""


