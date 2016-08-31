# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import time

config = {
    'user': 'soogic',
    'password': 'SniperX4',
    'host': '192.168.1.200',
    'database': 'scrapy'
}


# config = {
#     'user': 'root',
#     'password': 'SniperX4',
#     'host': 'localhost',
#     'database': 'scrapy'
# }


def get_current_timestamp():
    return int(round(time.time()))


def get_all_url_md5():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = 'select url_md5, title_md5 from scrapy.scrapy'
    url_md5_list = []
    try:
        cursor.execute(query)
        result_set = cursor.fetchall()
        for url_md5 in result_set:
            url_md5_list.append(url_md5[0])
            url_md5_list.append(url_md5[1])
        return url_md5_list
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


def save(url_md5, title_md5, title, abstract, url, keyword, hot_word, status):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        add_data_param = (
            "INSERT INTO scrapy (url_md5, title_md5, title, abstract, "
            "url, keyword, hotword, status, create_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_param = (
            url_md5, title_md5, title, abstract, url, keyword, hot_word, status, get_current_timestamp())

        cursor.execute(add_data_param, data_param)
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


def get_email_content():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = 'select title, abstract, url, keyword, hotword from scrapy.scrapy where status=0'
    try:
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
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
