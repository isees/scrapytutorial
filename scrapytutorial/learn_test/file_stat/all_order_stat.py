# -*- coding: utf-8 -*-

import json
import sys

all_order_file = 'C:\Users\Bain\Desktop\物流单汇总.txt'

all_order = open(all_order_file.decode('utf8').encode('gbk'), 'r')

shop_list = {}
for line in all_order.readlines():
    shop_name = line.split('|.|')[1].rstrip()
    if shop_list.has_key(shop_name) == False:
        shop_list[shop_name] = 0
    shop_list[shop_name] += 1

for shop in shop_list:
    print '%s\t%d' % (shop, shop_list[shop])
