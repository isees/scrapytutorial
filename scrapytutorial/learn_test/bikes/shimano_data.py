# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import time

# config = {
#     'user': 'soogic',
#     'password': 'SniperX4',
#     'host': '192.168.1.200',
#     'database': 'shimano'
# }

config = {
    'user': 'root',
    'password': 'SniperX4',
    'host': 'localhost',
    'database': 'scrapy'
}


source_dict = {
    1: "baidu",
    2: "yahoo"
}


def get_current_timestamp():
    return int(round(time.time()))


def get_keyword_list(file_path):
    words = []
    word_file = open(file_path)
    for line in word_file:
        if line.strip() != "":
            words.append(line.strip())
    return words


def get_all_url_md5():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = 'select url_md5, title_md5 from shimano.shimano'
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


def save(info_source, name_md5, name, fitting_class, fitting_series, fitting_model, fitting_brand, fitting_type, fitting_features, fitting_attributes, fitting_image_origin, fitting_image_standard, detail_url):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        add_data_param = (
            "INSERT INTO scrapy.shimano (info_source, name_md5, name, fitting_class, "
            "fitting_series, fitting_model, fitting_brand, fitting_type, fitting_features, fitting_attributes, "
            "fitting_image_origin, fitting_image_standard, detail_url, create_time, update_time) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_param = (
            info_source, name_md5, name, fitting_class, fitting_series, fitting_model, fitting_brand, fitting_type, fitting_features,
            fitting_attributes, fitting_image_origin, fitting_image_standard, detail_url, get_current_timestamp(), get_current_timestamp())

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


def udpate_status(source):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        update_sql = ("update shimano set status=1 where status=0 and source=%d" % source)
        cursor.execute(update_sql)
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
    query = 'select title, abstract, url, keyword, hotword, source from shimano.shimano where status=0'
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


def group_email_info(title, abstract, url, keyword, hotword, source):
    content = "\r\n"
    content += '%s [%s %s] - %s\r\n' % (title, keyword, hotword, source_dict[source])
    content += "        " + abstract + "\r\n"
    content += "        " + url + "\r\n"
    return content


def assemble_content():
    email_content = ""
    rs = get_email_content()
    for info in rs:
        title = info[0]
        abstract = info[1]
        url = info[2]
        keyword = info[3]
        hotword = info[4]
        source = info[5]
        email_content += group_email_info(title, abstract, url, keyword, hotword, source)
    return email_content
