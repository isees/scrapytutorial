import json
import random
import requests
from bs4 import BeautifulSoup

url = 'http://wx.miaoe.com/wxinquiry/miaomugongying.html'
dir_name = "miaoe"
file_path = '../../doc/' + dir_name + '/supplier_list.json'
save_path = "../../doc/" + dir_name + "/saved_info.txt"
# saved_file = open(save_path, 'wb')

headers = {
    "Host": "wx.miaoe.com",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6 Build/MOB30O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Crosswalk/17.46.448.10 Mobile Safari/537.36",
    # "Authorization": "Bearer eyJraWQiOiJhMTE3ZTA5Ny1jNWJiLTRmZTQtYTMwMC00MjE4NWI4MGY2MDYiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpc3N1ZXIiLCJhdWQiOiJhdWRpZW5jZSIsImV4cCI6MTQ3MDk4MjYwMCwianRpIjoiaVRGdWFMTGdocmM0azlVZm9lQTdNQSIsImlhdCI6MTQ3MDM4MzYwOCwibmJmIjoxNDcwMzgzNDg4LCJzdWIiOiIxODk4ODk5MjQ5MiIsImF0dHJpYnV0ZXMiOiJ7XCJhZGRyZXNzXCI6bnVsbCxcInN1cHBsaWVySWRcIjpudWxsLFwic3VwcGxpZXJcIjpudWxsLFwibG9naW5QYXNzd29yZFwiOm51bGwsXCJtb2JpbGVcIjpcIjE4OTg4OTkyNDkyXCIsXCJuYW1lXCI6XCLlp5pcIixcInZhbGlkYXRlQ29kZVwiOlwiOTA0NFwiLFwiaWRcIjpcIjU3MjA0YjgyMGNmMmZmMjExNDkzYjllOVwiLFwiJGV4cGlyYXRpb24tdGltZVwiOjE0NzA5ODI2MDAyMzksXCJhdWRpdFN0YXRlXCI6bnVsbCxcImN1cnJlbnRQb2ludFwiOjB9In0.i8jR9W4hHXf3AhwR3bVc4sG5MrFIwCZbnZ39c9cZQvqg754XJmcXpK6xoA92I_EKZcd2_t1J1npRk_qr5HXg-hjx5-Pfw5cks4EdU-bxZG4WL9AqtETp7RtUqy-8zt6Ek16baHjzSX0UfdjqBLErheHScoDH_B89VEZRBSH4XuzRWd7ClR-aQ0cMKWa2APsEmRlyE2lNQMDxjNsKLNmMqETgWxeu6wrX8Fe8n0P3IFHbTc61mMPai5s_vMw4HCobFrJmlWrRGtCMPeru2aMqsN1C1Qu3-1MXr26Ezx5HOWpSwrxgnHaBZdRADCntVrxEjRrPBeTZBJ-cPstPPGGUjA",
}


def string_to_json(line):
    return json.loads(line)


def get_next_param(currentIndex):
    param = {
        "currentPage": currentIndex,
        "pageAction": "next"
    }
    return param


def get_mobile():
    for index in range(0, 1):
        response = requests.post(url, data=get_next_param(index), headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # print soup.title
        # print soup.title.name
        # print soup.title.string
        # print soup.title.parent.name
        # print soup.p
        # print soup.p['class']
        # print soup.a
        # print soup.find_all('a')
        list = soup.find(class_='wxinq-list').find_all(class_='row')
        for row in list:
            name = row.find(class_='hdLinkman').get('value')
            mobile = row.find(class_='hdMobile').get('value')
            hdArea = row.find(class_='hdArea').get('value')
            companyName = row.find(class_='companyName').get('value')
            shopIcon = row.find(class_='shopIcon').get('data-id')
            authIcon = row.find(class_='auth-icon').string
            print name, mobile, companyName, shopIcon, authIcon


get_mobile()



#
#
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
