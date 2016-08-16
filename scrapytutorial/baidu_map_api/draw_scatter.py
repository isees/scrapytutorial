# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

x = [30, 0.12, 89, 857, 86]
y = [231, 432, 432, 1234, 232]
z = ['a', 'b', 'c', 'd', 'e']
fig = plt.figure()
ax = fig.add_subplot(111)
t = ax.scatter(x, y)
# ax.collections  # 返回的对象已经添加进了collections列表中

for key in range(len(x)):
    print '[%f,%f]' % (x[key], y[key])
    ax.annotate('[%s]' % (z[key]), xy=(x[key], y[key]), xycoords='data',
                xytext=(x[key]-100, y[key]-100), textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.08),
                horizontalalignment='right', verticalalignment='top',
                )
plt.show()
