%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, 'o', color='black');

# 传递给函数的第三个参数是使用一个字符代表的图表绘制点的类型。
# 就像你可以使用'-'或'--'来控制线条的风格那样
# 点的类型风格也可以使用短字符串代码来表示
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker, label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);

plt.plot(x, y, '-ok');

# plt.plot还有很多额外的关键字参数用来指定广泛的线条和点的属性
plt.plot(x, y, '-p', color='grey',
         markersize=15, linewidth=4,
         markerfacecolor='white', 
         markeredgecolor='grey',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2);

# 第二种更强大的绘制散点图的方法是使用plt.scatter函数
plt.scatter(x, y, marker='o');

# plt.scatter可以针对每个点设置不同属性（大小、填充颜色、边缘颜色等）
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
# alpha关键字参数对点的透明度进行了调整
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
# plt.colorbar() 在图像上生成颜色对比条
plt.colorbar();


"""鸢尾花数据集展示"""
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);


