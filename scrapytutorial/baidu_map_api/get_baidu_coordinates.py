# -*- coding: utf-8 -*-

# 第一行必须有，否则报中文字符非ascii码错误
import urllib
import hashlib
import requests
import json

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

service_url = 'http://api.map.baidu.com/geocoder/v2/'
ak = 'cGGHb7UCTowSDhtokRz9S0SE5aE7Zm9e'
sk = '9gPwX4aVgDRGGUpH3uXiEqdhu6cAV7le'

file_path = "D:\workspace\python\scrapytutorial\doc\locations.txt"
save_path = "D:\workspace\python\scrapytutorial\doc\\x_locations.txt"


def get_coodinates(address):
    # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
    queryStr = '/geocoder/v2/?address=%s&output=json&ak=%s' % (address, ak)

    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

    # 在最后直接追加上yoursk
    rawStr = encodedStr + sk

    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
    url = service_url + '?address=%s&output=json&ak=%s&sn=%s' % (address, ak, sn)
    print url
    content = requests.get(url).content
    print content
    return json.loads(content)


def get_locations(file_path):
    file_array = []
    for line in open(file_path).readlines():
        file_array.append(line)
    return file_array


location_array = get_locations(file_path)
save_file = open(save_path, 'wb')
for index in range(len(location_array)):
    infos = location_array[index].strip()
    info_array = infos.split("|.|")
    name = info_array[0]
    mobile = info_array[1]
    province = info_array[2]
    city = info_array[3]
    district = info_array[4]
    address = info_array[5]
    # print index, province, city, district, address

    search_location = province + city + district + address
    print search_location
    jcon = get_coodinates(search_location)
    print jcon
    print jcon['result']
    lng = jcon['result']['location']['lng']
    lat = jcon['result']['location']['lat']
    precise = jcon['result']['precise']
    confidence = jcon['result']['confidence']
    level = jcon['result']['level']
    save_file.write(infos)
    save_file.write('|.|%f' % lng)
    save_file.write('|.|%f' % lat)
    save_file.write('|.|%d' % precise)
    save_file.write('|.|%d' % confidence)
    save_file.write('|.|%s' % level)
    save_file.write("\n")
