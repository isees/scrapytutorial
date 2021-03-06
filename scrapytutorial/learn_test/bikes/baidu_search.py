# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import json
import hashlib
import scrapy_data as sd
import email_controller as  sender
import random
import sys
from  baidu_hot import get_hot_start_list

reload(sys)
sys.setdefaultencoding("utf-8")

one_year_ago = 1
one_month_ago = 2
one_week_ago = 3
last_24_hour = 4

source_dict = {
    1: "百度",
    2: "yahoo"
}


def get_current_timestamp():
    return int(round(time.time()))


def get_date_type_value(now_time, date_type=0):
    switcher = {
        1: now_time - 366 * 24 * 3600,
        2: now_time - 31 * 24 * 3600,
        3: now_time - 7 * 24 * 3600,
        4: now_time - 24 * 3600
    }
    return switcher.get(date_type, None)


def get_real_url(search_url):
    try:
        response = requests.get(search_url, timeout=15)
        return response.url
    except Exception, err:  # This is the correct syntax
        print err.message
    return search_url


def generate_search_url(search_word, date_type=0):
    search_list_url = 'https://www.baidu.com/s?wd=%s' % search_word
    now_time = get_current_timestamp()
    start_time = get_date_type_value(now_time, date_type)
    if start_time is not None:
        search_date_param = '&gpc=stf%%3D%d%%2C%d%%7Cstftype%%3D1' % (start_time, now_time)
        search_list_url += search_date_param
    return search_list_url


headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8,ar;q=0.6",
    "Cache-Control": "no-cache",
    "Host": "www.baidu.com",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    # "Cookie": "BAIDUID=8D27927E1211A6FD34BE0D6F2A4C1630:FG=1; PSTM=1467911842; BIDUPSID=2726F935573AC522580E279FCAF6B311; sugstore=1; pgv_pvi=8610781184; ispeed_lsm=0; BD_HOME=0; BD_UPN=12314753; H_PS_645EC=d572WSqnwzErF4Vhplk%2B5xcVawDM2r7E8bV3vWsX1yn33RXbC8Qs%2FPKYdH4; BD_CK_SAM=1; BDSVRTM=17; H_PS_PSSID=1420_18280_18560_17001_11655_20856_20733_20837; __bsi=17440691342695070569_00_0_I_R_19_0303_C02F_N_I_I_0"
}


def save_searched_content(keyword, hot_word, date_type, source=1):
    search_url = generate_search_url('%s %s' % (hot_word, keyword), date_type)
    result = requests.get(search_url, headers=headers)
    html = result.content
    soup = BeautifulSoup(html, 'html.parser')

    url_md5_list = sd.get_all_url_md5()

    if soup.find(id='content_left') is not None:
        for group in soup.find(id='content_left').find_all("div", class_="result"):
            # print json.dumps(group.h3.a.contents, ensure_ascii=False)
            try:
                title = group.h3.a.text
                title_md5 = hashlib.md5(title.encode('utf-8')).hexdigest()
                abstract = group.find("div", class_='c-abstract').text

                if hot_word not in title and hot_word not in abstract:
                    print '%s not found' % hot_word
                    continue

                if title_md5 in url_md5_list:
                    print '<<%s>> exists' % title
                    continue
                url_md5_list.append(title_md5)

                url = get_real_url(group.h3.a.get("href"))
                url_md5 = hashlib.md5(url.encode('utf-8')).hexdigest()
                if url_md5 in url_md5_list:
                    print '"%s" exists' % url
                    continue
                url_md5_list.append(url_md5)

                print title, ' [%s %s]' % (keyword, hot_word)
                print abstract
                print url
                print '\n'

                sd.save(url_md5, title_md5, title, abstract, url, keyword, hot_word, 0, 1)
            except Exception, err:
                print err.message
                continue


def search_and_save():
    keywords = sd.get_keyword_list('D:\workspace\python\scrapytutorial\doc\soogic\keywords')
    hot_words = set(
        sd.get_keyword_list('D:\workspace\python\scrapytutorial\doc\soogic\hotwords') + get_hot_start_list())
    for hot_word in hot_words:
        for keyword in keywords:
            save_searched_content(keyword, hot_word, one_year_ago)


search_and_save()

