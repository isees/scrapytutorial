# -*- coding: utf-8 -*-

import sys
import json
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://wx.miaoe.com/wxinquiry/miaomugongying.html'
shop_list_url = 'http://wx.miaoe.com/wxinquiry/shop-[shop_id].html'

dir_name = "miaoe"
file_path = '../../doc/' + dir_name + '/supplier_list.json'
save_path = "../../doc/" + dir_name + "/saved_info.txt"
# saved_file = open(save_path, 'wb')

area_list = [{"code": "44", "name": "广东省"}, {"code": "53", "name": "云南省"}, {"code": "45", "name": "广西省"},
             {"code": "13", "name": "河北省"}, {"code": "14", "name": "山西省"}, {"code": "12", "name": "天津市"},
             {"code": "15", "name": "内蒙古"}, {"code": "11", "name": "北京市"}, {"code": "35", "name": "福建省"},
             {"code": "37", "name": "山东省"}, {"code": "31", "name": "上海市"}, {"code": "32", "name": "江苏省"},
             {"code": "33", "name": "浙江省"}, {"code": "34", "name": "安徽省"}, {"code": "46", "name": "海南省"},
             {"code": "36", "name": "江西省"}, {"code": "41", "name": "河南省"}, {"code": "42", "name": "湖北省"},
             {"code": "43", "name": "湖南省"}, {"code": "51", "name": "四川省"}, {"code": "50", "name": "重庆市"},
             {"code": "52", "name": "贵州省"}, {"code": "54", "name": "西藏"}, {"code": "61", "name": "陕西省"},
             {"code": "62", "name": "甘肃省"}, {"code": "63", "name": "青海省"}, {"code": "64", "name": "宁夏"},
             {"code": "65", "name": "新疆"}, {"code": "21", "name": "辽宁省"}, {"code": "22", "name": "吉林省"},
             {"code": "23", "name": "黑龙江省"}]

# for x in area_list:
#     print json.dumps(x, ensure_ascii=False, encoding='utf-8')

shop_id_cache = []

headers = {
    "Host": "wx.miaoe.com",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6 Build/MOB30O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Crosswalk/17.46.448.10 Mobile Safari/537.36",
    "Referer": "http://wx.miaoe.com/wxinquiry/miaomugongying.html",
    # "Authorization": "Bearer eyJraWQiOiJhMTE3ZTA5Ny1jNWJiLTRmZTQtYTMwMC00MjE4NWI4MGY2MDYiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpc3N1ZXIiLCJhdWQiOiJhdWRpZW5jZSIsImV4cCI6MTQ3MDk4MjYwMCwianRpIjoiaVRGdWFMTGdocmM0azlVZm9lQTdNQSIsImlhdCI6MTQ3MDM4MzYwOCwibmJmIjoxNDcwMzgzNDg4LCJzdWIiOiIxODk4ODk5MjQ5MiIsImF0dHJpYnV0ZXMiOiJ7XCJhZGRyZXNzXCI6bnVsbCxcInN1cHBsaWVySWRcIjpudWxsLFwic3VwcGxpZXJcIjpudWxsLFwibG9naW5QYXNzd29yZFwiOm51bGwsXCJtb2JpbGVcIjpcIjE4OTg4OTkyNDkyXCIsXCJuYW1lXCI6XCLlp5pcIixcInZhbGlkYXRlQ29kZVwiOlwiOTA0NFwiLFwiaWRcIjpcIjU3MjA0YjgyMGNmMmZmMjExNDkzYjllOVwiLFwiJGV4cGlyYXRpb24tdGltZVwiOjE0NzA5ODI2MDAyMzksXCJhdWRpdFN0YXRlXCI6bnVsbCxcImN1cnJlbnRQb2ludFwiOjB9In0.i8jR9W4hHXf3AhwR3bVc4sG5MrFIwCZbnZ39c9cZQvqg754XJmcXpK6xoA92I_EKZcd2_t1J1npRk_qr5HXg-hjx5-Pfw5cks4EdU-bxZG4WL9AqtETp7RtUqy-8zt6Ek16baHjzSX0UfdjqBLErheHScoDH_B89VEZRBSH4XuzRWd7ClR-aQ0cMKWa2APsEmRlyE2lNQMDxjNsKLNmMqETgWxeu6wrX8Fe8n0P3IFHbTc61mMPai5s_vMw4HCobFrJmlWrRGtCMPeru2aMqsN1C1Qu3-1MXr26Ezx5HOWpSwrxgnHaBZdRADCntVrxEjRrPBeTZBJ-cPstPPGGUjA",
    # "Cookie": "JSESSIONID=E07B5268366E2799362E9D5B05A30476; haibao=inquiryhaibao; Hm_lvt_0237eefc348658d245c327551d667ed5=1471343475; Hm_lpvt_0237eefc348658d245c327551d667ed5=1471343475; CNZZDATA1000124037=787208071-1470966405-%7C1471397731",
}


def get_province_list(index=0):
    province_url = 'http://wx.miaoe.com/wxinquiry/area/areaAction!getProv.do'
    response = requests.get(province_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    prov_json = json.loads(soup.string)
    for prov in prov_json['data']:
        area_list.append(
            {
                'code': prov['code'],
                'name': prov['name']
            }
        )
    print json.dumps(area_list, ensure_ascii=False, encoding='utf-8')

    # for area in area_list:
    #     print json.dumps(area, ensure_ascii=False, encoding='utf-8')


def get_next_param(currentIndex, area='', code=''):
    param = {
        # "searchName": "",
        # "name": "",
        # "crown": "",
        # "height": "",
        # "dbh": "",
        "fullName": area,
        # "type": "",
        "encode": code,
        "currentPage": currentIndex,
        "pageAction": "next"
    }
    return param


def get_index_info():
    for area in area_list:
        code = area['code']
        name = area['name']

        print name, code

        for index in range(0, 1):
            response = requests.post(url, params=get_next_param(index, name, code), headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            list = soup.find(class_='wxinq-list').find_all(class_='row')

            for row in list:
                shopIcon = row.find(class_='shopIcon').get('data-id')
                if shopIcon in shop_id_cache:
                    continue
                else:
                    shop_id_cache.append(shopIcon)
                name = row.find(class_='hdLinkman').get('value')
                authIcon = row.find(class_='auth-icon').string
                mobile = row.find(class_='hdMobile').get('value')
                hdArea = row.find(class_='hdArea').get('value')
                companyName = row.find(class_='companyName').get('value')
                shopIcon = row.find(class_='shopIcon').get('data-id')
                hdRemark = row.find(class_='hdRemark').get('value')
                print shopIcon, name, authIcon, mobile, hdArea, companyName, hdRemark
                # remark_array = get_shop_list(shopIcon)
                # print json.dumps(remark_array, ensure_ascii=False, encoding='utf-8')


def get_shop_list(shop_id, current_index=0):
    remark_array = []
    url = shop_list_url.replace('[shop_id]', shop_id)
    print current_index
    response = requests.post(url, params=get_next_param(current_index), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    list = soup.find(class_='wxinq-list').find_all(class_='row')
    for row in list:
        business = row.find(class_='hdRemark').get('value')
        remark_array.append(business)

    paging = soup.find(class_='paging')
    if paging.find(class_='btnNext') != None and 'disabled' not in paging.find(class_='btnNext')['class']:
        current_index += 1
        remark_array += get_shop_list(shop_id, current_index)

    return remark_array


get_index_info()
# get_province_list()



# shop_id = 'e9aec36a64d04840a03e35f33c561939'
# get_shop_list(shop_id)


# def string_to_json(line):
#    return json.loads(line)
#
# with open(file_path) as list_file:
#     for line in list_file:
#         json_content = string_to_json(line)
#         result = json_content[0]['result']
#         page = result['page']
#         content = page['content']
#         for element in content:
#             # element['id']
#             # element['shopName']
#             # element['remark']
#             # element['business']
#             # element['address']
#             # element['area']
#             print '%s||%s||%s||%s||%s||%s||%s' % (
#                 element['id'], element['shopName'], element['business'], element['address'], element['area'],
#                 element['productNum'], element['dateCreated'])
#
#             print '%s' % str(element['id'])
#             mobile = get_mobile(str(element['id']))
#             print '%s' % mobile
#
#             line_info = '%s||%s||%s||%s||%s||%s||%s||%s' % (
#                 element['id'], element['shopName'], element['business'], element['address'], element['area'],
#                 element['productNum'], element['dateCreated'], mobile)
#
#             saved_file.write(line_info.encode('utf-8').strip())
#             saved_file.write('\n')
#
# list_file.close()
