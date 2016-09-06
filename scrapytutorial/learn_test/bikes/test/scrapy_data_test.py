# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import time
import numpy
from itertools import chain

config = {
    'user': 'soogic',
    'password': 'SniperX4',
    'host': '192.168.1.200',
    'database': 'scrapy'
}


def get_current_timestamp():
    return int(round(time.time()))


def save(url_md5, title_md5, title, abstract, url, status):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        add_data_param = (
            "INSERT INTO scrapy (url_md5, title_md5, title, abstract, "
            "url, status, create_time) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data_param = (
            url_md5, title_md5, title, abstract, url, status, get_current_timestamp())

        cursor.execute(add_data_param, data_param)
        cnx.commit()
    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Something is wrong with your user name or password")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database does not exist")
    #     else:
    #         print(err)
    finally:
        cursor.close()
        cnx.close()


def get_all_url_md5():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = 'select url_md5 from scrapy.scrapy'
    try:
        cursor.execute(query)
        result_set = cursor.fetchall()
        print '0ffce08ce223eabd1d97d1438e384da2' in result_set
        url_md5_list = []
        for url_md5 in result_set:
            url_md5_list.append(url_md5[0])
        print '0ffce08ce223eabd1d97d1438e384da2' in url_md5_list
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


# get_all_url_md5()
# save('cc2c8c54686e5d6bf51d82f0ff83196d', 'afd790d5dc259b765f80e176268c5145', '第十三讲 ionic css布局介绍 - ionic 教程',
#      '2016年8月18日 - 所以又看了一下其他的框架,比如:Lungo和QuoJS等,突然发现了一个目前比较先进的框架ionic,所以就拿来用用。目前文档比较少,有的也仅是翻译官网的,所以...',
#      ' http://www.ithtw.com/1702.html', 0)
