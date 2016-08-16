# -*- coding: utf-8 -*-

# 第一行必须有，否则报中文字符非ascii码错误
import urllib
import hashlib
import requests
import json

from pylab import *
import numpy as np
import matplotlib.pyplot as plt

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

save_path = "D:\workspace\python\scrapytutorial\doc\\x_locations.txt"


def get_locations(file_path):
    file_array = []
    for line in open(file_path).readlines():
        file_array.append(line)
    return file_array


x = []
y = []
z = []

location_array = get_locations(save_path)
for index in range(len(location_array)):
    infos = location_array[index].strip()
    info_array = infos.split("|.|")
    name = info_array[0]
    mobile = info_array[1]
    province = info_array[2]
    city = info_array[3]
    district = info_array[4]
    address = info_array[5]
    lng = info_array[6]
    lat = info_array[7]
    x.append(float(lng))
    y.append(float(lat))
    z.append(name)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y)
for key in range(len(x)):
    # if key > 50:
    #     break
    ax.annotate('the top',
                xy=(x[key], y[key]),  # theta, radius
                xytext=(x[key], x[key]),  # theta, radius
                xycoords='data',
                textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.01),
                horizontalalignment='left',
                verticalalignment='bottom',
                clip_on=True,  # clip to the axes bounding box
                )
ax.set_xlim(113.203, 113.502)
ax.set_ylim(22.9318, 23.2627)
plt.show()
