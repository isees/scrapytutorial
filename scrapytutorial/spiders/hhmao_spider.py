import json
import random
import requests

file_path = '../../doc/supplier_list.json'

url = 'https://hhmao.com/web-rpc'

headers = {
    "Host": "hhmao.com",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6 Build/MOB30O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Crosswalk/17.46.448.10 Mobile Safari/537.36",
    "Authorization": "Bearer eyJraWQiOiJhMTE3ZTA5Ny1jNWJiLTRmZTQtYTMwMC00MjE4NWI4MGY2MDYiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpc3N1ZXIiLCJhdWQiOiJhdWRpZW5jZSIsImV4cCI6MTQ3MDk4MjYwMCwianRpIjoiaVRGdWFMTGdocmM0azlVZm9lQTdNQSIsImlhdCI6MTQ3MDM4MzYwOCwibmJmIjoxNDcwMzgzNDg4LCJzdWIiOiIxODk4ODk5MjQ5MiIsImF0dHJpYnV0ZXMiOiJ7XCJhZGRyZXNzXCI6bnVsbCxcInN1cHBsaWVySWRcIjpudWxsLFwic3VwcGxpZXJcIjpudWxsLFwibG9naW5QYXNzd29yZFwiOm51bGwsXCJtb2JpbGVcIjpcIjE4OTg4OTkyNDkyXCIsXCJuYW1lXCI6XCLlp5pcIixcInZhbGlkYXRlQ29kZVwiOlwiOTA0NFwiLFwiaWRcIjpcIjU3MjA0YjgyMGNmMmZmMjExNDkzYjllOVwiLFwiJGV4cGlyYXRpb24tdGltZVwiOjE0NzA5ODI2MDAyMzksXCJhdWRpdFN0YXRlXCI6bnVsbCxcImN1cnJlbnRQb2ludFwiOjB9In0.i8jR9W4hHXf3AhwR3bVc4sG5MrFIwCZbnZ39c9cZQvqg754XJmcXpK6xoA92I_EKZcd2_t1J1npRk_qr5HXg-hjx5-Pfw5cks4EdU-bxZG4WL9AqtETp7RtUqy-8zt6Ek16baHjzSX0UfdjqBLErheHScoDH_B89VEZRBSH4XuzRWd7ClR-aQ0cMKWa2APsEmRlyE2lNQMDxjNsKLNmMqETgWxeu6wrX8Fe8n0P3IFHbTc61mMPai5s_vMw4HCobFrJmlWrRGtCMPeru2aMqsN1C1Qu3-1MXr26Ezx5HOWpSwrxgnHaBZdRADCntVrxEjRrPBeTZBJ-cPstPPGGUjA",
}


def string_to_json(line):
    return json.loads(line)


save_path = "../../doc/saved_info.txt"

saved_file = open(save_path, 'wb')


def get_mobile_params(supplier_id):
    x =  [{'id': 'id' + str(random.randint(1000000000, 9999999999)),
             'name': 'supplierWebRpc.showSupplierMobile',
             'args': ["\"%s\"" % supplier_id, "\"%d\"" % random.randint(10000000000, 19999999999)]}]
    print x
    return x

def get_mobile(supplier_id):
    mobile_info = requests.post(url, json=get_mobile_params(supplier_id), headers=headers)
    mobile_number = string_to_json(mobile_info.content)[0]['result']
    return mobile_number


with open(file_path) as list_file:
    for line in list_file:
        json_content = string_to_json(line)
        result = json_content[0]['result']
        page = result['page']
        content = page['content']
        for element in content:
            # element['id']
            # element['shopName']
            # element['remark']
            # element['business']
            # element['address']
            # element['area']
            print '%s||%s||%s||%s||%s||%s||%s' % (
                element['id'], element['shopName'], element['business'], element['address'], element['area'],
                element['productNum'], element['dateCreated'])

            print '%s' % str(element['id'])
            mobile = get_mobile(str(element['id']))
            print '%s' % mobile

            line_info = '%s||%s||%s||%s||%s||%s||%s||%s' % (
                element['id'], element['shopName'], element['business'], element['address'], element['area'],
                element['productNum'], element['dateCreated'], mobile)

            saved_file.write(line_info.encode('utf-8').strip())
            saved_file.write('\n')

list_file.close()
