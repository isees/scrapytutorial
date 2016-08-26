# coding: utf-8

app_stat_file = 'D:\workspace\python\scrapytutorial\doc\\active_user_stat\\app_order_stat.txt'
shop_stat_file = 'D:\workspace\python\scrapytutorial\doc\\active_user_stat\\all_order_stat.txt'

stat_list = {}


def get_stat_list(file_path):
    shop_list = open(file_path, 'rb')
    for line in shop_list:
        stat = line.split('\t')
        name = stat[0].strip()
        count = int(stat[1].strip())
        if name in stat_list.keys():
            continue
        stat_list[name] = count
    return stat_list


get_stat_list(shop_stat_file)
get_stat_list(app_stat_file)

app_exists_file = 'D:\workspace\python\scrapytutorial\doc\\active_user_stat\shop_exists_but_app.txt'
app_list = open(app_exists_file, 'rb')

for app_shop in app_list:
    name = app_shop.strip()
    if name in stat_list:
        print name + '\t' + str(stat_list[name])
    else:
        print name
