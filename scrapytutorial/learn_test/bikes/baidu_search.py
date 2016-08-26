# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time


def get_current_timestamp():
    return int(round(time.time()))


search_word = "ionic 速成"
now_time = get_current_timestamp()
one_year_ago = now_time - 366 * 24 * 3600
one_month_ago = now_time - 31 * 24 * 3600
one_week_ago = now_time - 7 * 24 * 3600
last_24_hour = now_time - 24 * 3600

print now_time, one_year_ago

search_list_url = 'https://www.baidu.com/s?wd=%s&gpc=stf%%3D%d%%2C%d%%7Cstftype%%3D1' % (
    search_word, one_month_ago, now_time)
print search_list_url

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

result = requests.get(search_list_url, headers=headers)
html = result.content
soup = BeautifulSoup(html, 'html.parser')
if soup.find(id='content_left') != None:
    for group in soup.find(id='content_left').find_all("div", class_="result"):
        print group
