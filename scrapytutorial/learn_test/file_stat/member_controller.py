# -*- coding: utf-8 -*-

import json
import sys
import month_array

app_file = open("D:\workspace\python\scrapytutorial\doc\\active_user_stat\\app_member")
all_file = open("D:\workspace\python\scrapytutorial\doc\\active_user_stat\\shop_member")
app_order_file = open("D:\workspace\python\scrapytutorial\doc\\active_user_stat\\app_order_stat.txt")

app_member = []
all_member = []
app_order_list = []

for line in app_file:
    if line.strip() not in app_member:
        app_member.append(line.strip())

for line in all_file:
    if line.strip() not in all_member:
        all_member.append(line.strip())

for line in app_order_file:
    name = line.split('\t')[0].strip()
    if name not in app_order_list:
        app_order_list.append(name)

# print json.dumps(app_member, ensure_ascii=False)
# print json.dumps(all_member, ensure_ascii=False)
# print json.dumps(app_order_list, ensure_ascii=False)

for app_order_shop in app_member:
    if app_order_shop not in app_order_list:
        print app_order_shop

# for shop_order_shop in all_member:
#     if shop_order_shop not in app_order_list:
#         print shop_order_shop