# -*- coding: utf-8 -*-

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

x = {"型号 ": "FD-M9025 ", "系列 ": "XTR ",
     "摆式操作 ": "下摆式 ", "兼容飞轮 ": "11 ", "最大换齿容量 ": "10T ", "高速齿 ": "38T "}

key = '型号'
if key in x.keys():
    print key, x[key]
