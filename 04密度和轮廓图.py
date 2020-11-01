"""
通过组合使用plt.contour、plt.contourf和plt.imshow这三个函数，
基本可以满足我们绘制所有这种在二维图标上的三维数据的需求。
"""

%matplotlib inline 
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10+y*x) * np.cos(x)

# 轮廓图可以使用plt.contour函数进行创建
"""
    x参数代表三维网格的平面横轴坐标
    y参数代表三维网格的平面纵轴坐标
    而z参数代表三维网格的高度坐标
    np.meshgrid函数，可以将两个一维的数组构造成一个二维的网格
""""

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='black');
# 当使用单色绘制轮廓图时，虚线代表的是负数的数值，而实线代表的是正数
# 轮廓线可以通过指定cmap参数来设置线条的色图

# RdGy（Red-Gray的缩写）色图，这对于聚集的数据来说是一个不错的选择
plt.contour(X, Y, Z, 20, cmap='RdGy');

# 填充轮廓图
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar();

# plt.imshow()函数，它会将一个二维的网格图表转换为一张图像
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image');
"""
在使用imshow()的时候也有一些坑:
plt.imshow()不接受 x 和 y 网格值作为参数，
    因此你需要手动指定extent参数[xmin, xmax, ymin, ymax]来设置图表的数据范围。
plt.imshow()使用的是默认的图像坐标，即左上角坐标点是原点，而不是通常图表的左下角坐标点。
    这可以通过设置origin参数来设置。
plt.imshow()会自动根据输入数据调整坐标轴的比例；
    这可以通过参数来设置，例如，plt.axis(aspect='image')能让 x 和 y 轴的单位一致。
"""

# 将轮廓图和图像结合起来
contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)
# 通过设置alpha设置参数透明度
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', camp='RdGy', alpha=0.5)
plt.colorbar();

