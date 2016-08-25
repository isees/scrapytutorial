# -*- coding: utf-8 -*-

import json
import sys

all_order_file = 'C:\Users\Bain\Desktop\\app订单.txt'

all_order = open(all_order_file.decode('utf8').encode('gbk'), 'r')

order_id_list = []
shop_count = {}
order_date_list = []

for line in all_order:
    split = line.split('|.|')
    order_id = split[3].strip()
    order_date = split[0].strip()
    shop_name = split[1].strip()
    if order_id in order_id_list:
        continue
    if order_date + "_" + shop_name in order_date_list:
        continue
    else:
        order_date_list.append(order_date + "_" + shop_name)
    order_id_list.append(order_id)
    if shop_count.has_key(shop_name) == False:
        shop_count[shop_name] = 0
    shop_count[shop_name] += 1

for shop_name in shop_count:
    print '%s\t%d' % (shop_name, shop_count[shop_name])
