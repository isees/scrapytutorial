# -*- coding: utf-8 -*-

import month_array


def add_zero(month):
    if len(month) < 2:
        month = '0' + month
    return month


def get_shop_count(file_path):
    app_shop_count = {}
    order_id_list = []
    order_date_list = []
    all_order = open(file_path.decode('utf8').encode('gbk'), 'r')
    for line in all_order:
        info = line.split('|.|')

        yeah_month_array = info[0].split("-")
        if yeah_month_array.__len__() >= 2:
            yeah_month = yeah_month_array[0] + add_zero(yeah_month_array[1])
        else:
            yeah_month = ''

        order_id = info[3].strip()
        order_date = info[0].strip()
        shop_name = info[1].strip()
        if order_id in order_id_list:
            continue
        if order_date + "_" + shop_name in order_date_list:
            continue

        order_date_list.append(order_date + "_" + shop_name)
        order_id_list.append(order_id)

        if app_shop_count.has_key(shop_name) == False:
            app_shop_count[shop_name] = {}
        if app_shop_count[shop_name].has_key(yeah_month) == False:
            app_shop_count[shop_name][yeah_month] = 0
        app_shop_count[shop_name][yeah_month] += 1
    return app_shop_count


all_order_file = 'C:\Users\Bain\Desktop\\app订单.txt'
app_shop_list = get_shop_count(all_order_file)

all_order = open('D:\workspace\python\scrapytutorial\doc\\active_user_stat\\app_order_stat.txt', 'rb')
month_array = month_array.get_and_print_month_array('201509', 12)
for shop in all_order:
    shop_name = shop.split('\t')[0]
    month_count = app_shop_list[shop_name]
    shop_month_count_str = ''
    for month in month_array:
        if month_count.has_key(month) == False:
            shop_month_count_str += '\t'
        else:
            shop_month_count_str += str(month_count[month]) + '\t'
    print shop_name + '\t' + shop_month_count_str
