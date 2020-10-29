# 折线图
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes()
x = np.linespace(0, 10, 1000)
ax.plot(x, np.sin(x));                          # or plt.plot(x, np.sin(x));

# 在同一幅图形中绘制多个线条，只需要多次调用plot函数
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));

# 调整折线图：线条颜色
plt.plot(x, np.sin(x-0), color='blue')          # 通过颜色名称指定
plt.plot(x, np.sin(x-1), color='g')             # 通过颜色简写名称指定(rgbcmyk)
plt.plot(x, np.sin(x-2), color='0.75')          # 介于0-1之间的灰阶值
plt.plot(x, np.sin(x-3), color=(1.0, 2.0, 3.0)  # RGB元组的颜色值，每个值介于0-1
plt.plot(x, np.sin(x-4), color='#FFDD44')       # 16进制的RRGGBB值
plt.plot(x, np.sin(x-5), color='chartreuse');   # 能支持所有HTML颜色名称值
# 如果没有指定颜色，matplotlib会循环使用不同颜色

# 设置线条风格
plt.plot(x, x+0, linestyle='solid')
plt.plot(x, x+1, linestyle='dashed')
plt.plot(x, x+2, linestyle='dashdot')
plt.plot(x, x+3, linestyle='dotted');

# 或者使用符号代替具体英文
plt.plot(x, x+4, linestyle='-')         # 实线
plt.plot(x, x+5, linestyle='--')        # 虚线
plt.plot(x, x+6, linestyle='-.')        # 长短点虚线
plt.plot(x, x+7, linestyle=':');        # 点线

# linestyle和color参数合并为同一个非关键字参数
plt.plot(x, x+0, '-g')                  # 绿色实线
plt.plot(x, x+1, '--c')                 # 天青色虚线
plt.plot(x, x+2, '-.k'0                 # 黑色长短点虚线
plt.plot(x, x+3, ':r');                 # 红色点线

# 调整折线图：坐标轴范围
plt.plot(x, np.sin(x))

# plt.xlim()和plt.ylim()函数可以调整坐标轴的范围
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);

# 坐标轴反向
plt.xlim(10, 0)
plt.ylim(1.2, -1.2);

# 相关的函数还有plt.axis(),这个函数可以在一个函数调用中就完成 x 轴和 y 轴范围的设置，传递一个[xmin, xmax, ymin, ymax]的列表参数即可
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5])

# plt.axis()函数可以将坐标轴压缩到刚好足够绘制折线图像的大小
plt.plot(x, np.sin(x))
plt.axis('tight');

# 设置'equal'参数设置X轴与Y轴使用相同的长度单位
plt.plot(x, np.sin(x))
plt.axis('equal');

# 折线图标签
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");


plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')

plt.legend();


# MATLAB 风格的函数
"""
plt.xlabel() → ax.set_xlabel()

plt.ylabel() → ax.set_ylabel()

plt.xlim() → ax.set_xlim()

plt.ylim() → ax.set_ylim()

plt.title() → ax.set_title()
"""
# 使用ax.set()方法来一次性设置所有的属性
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot');
       




