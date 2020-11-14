# 图例可以为可视化赋予实际含义，为不同的图标元素附上明确说明。
# plt.legend()函数来创建最简单的图例，这个函数能自动创建任何带有标签属性的图表元素的图例
import matplotlib.pyplot as plt
import numpy as np
plt.styple.use('classic')
%matplotlib inline

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', lable='Cosine')
