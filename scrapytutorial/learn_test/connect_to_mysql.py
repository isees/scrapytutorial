# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import time


def get_current_timestamp():
    return int(round(time.time()))


config = {
    'user': 'bain',
    'password': 'SniperX4',
    'host': '127.0.0.1',
    'database': 'flower_scrapy'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

try:

    add_shop_info = (
        "INSERT INTO raw_data (unique_tag, supplier_name, supplier_phone, area, "
        "address, shop_name, is_confirmed, remark, create_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data_shop_info = (
        '86a358fa3f3041a2abd992169d3e10f3', '刘永乾', '13503226209', '河北省', '河北省保定市', '华谊园林', 0, '梅花树推广基地',
        get_current_timestamp())

    cursor.execute(add_shop_info, data_shop_info)
    cnx.commit()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    cursor.close()
    cnx.close()
