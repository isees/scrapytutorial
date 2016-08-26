# -*- coding: utf-8 -*-

import json
import sys
import month_array


def add_zero(month):
    if len(month) < 2:
        month = '0' + month
    return month


def fill_stat_shop_list(file_path):
    shop_list = {}
    all_order = open(file_path.decode('utf8').encode('gbk'), 'r')
    for line in all_order.readlines():
        info = line.split('|.|')
        yeah_month_array = info[0].split("-")
        if yeah_month_array.__len__() >= 2:
            yeah_month = yeah_month_array[0] + add_zero(yeah_month_array[1])
        else:
            yeah_month = ''
        shop_name = info[1].rstrip()
        if shop_list.has_key(shop_name) == False:
            shop_list[shop_name] = {}
        if shop_list[shop_name].has_key(yeah_month) == False:
            shop_list[shop_name][yeah_month] = 0
        shop_list[shop_name][yeah_month] += 1
    return shop_list


def get_app_shop_list(file_path):
    app_shop_list = []
    app_file = open(file_path, 'rb')
    for line in app_file:
        app_shop_list.append(line.split('\t')[0])
    return app_shop_list


all_order_file = 'C:\Users\Bain\Desktop\物流单汇总.txt'
app_order_file = 'D:\workspace\python\scrapytutorial\doc\\active_user_stat\\app_order_stat.txt'

shop_list = fill_stat_shop_list(all_order_file)
app_shop_list = get_app_shop_list(app_order_file)

all_order = open('D:\workspace\python\scrapytutorial\doc\\active_user_stat\\all_order_stat.txt', 'rb')
month_array = month_array.get_and_print_month_array('201509', 12)
for shop in all_order:
    shop_name = shop.split('\t')[0]
    if shop_name in app_shop_list:
        continue
    month_count = shop_list[shop_name]
    shop_month_count_str = ''
    for month in month_array:
        if month_count.has_key(month) == False:
            shop_month_count_str += '\t'
        else:
            shop_month_count_str += str(month_count[month]) + '\t'
    print shop_name + '\t' + shop_month_count_str
