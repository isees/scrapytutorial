import requests
import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://hhmao.com/web-rpc'

headers = {
    "Host": "hhmao.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-us",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6 Build/MOB30O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Crosswalk/17.46.448.10 Mobile Safari/537.36",
    # "Authorization": "Bearer eyJraWQiOiJhMTE3ZTA5Ny1jNWJiLTRmZTQtYTMwMC00MjE4NWI4MGY2MDYiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpc3N1ZXIiLCJhdWQiOiJhdWRpZW5jZSIsImV4cCI6MTQ3MDk4MjYwMCwianRpIjoiaVRGdWFMTGdocmM0azlVZm9lQTdNQSIsImlhdCI6MTQ3MDM4MzYwOCwibmJmIjoxNDcwMzgzNDg4LCJzdWIiOiIxODk4ODk5MjQ5MiIsImF0dHJpYnV0ZXMiOiJ7XCJhZGRyZXNzXCI6bnVsbCxcInN1cHBsaWVySWRcIjpudWxsLFwic3VwcGxpZXJcIjpudWxsLFwibG9naW5QYXNzd29yZFwiOm51bGwsXCJtb2JpbGVcIjpcIjE4OTg4OTkyNDkyXCIsXCJuYW1lXCI6XCLlp5pcIixcInZhbGlkYXRlQ29kZVwiOlwiOTA0NFwiLFwiaWRcIjpcIjU3MjA0YjgyMGNmMmZmMjExNDkzYjllOVwiLFwiJGV4cGlyYXRpb24tdGltZVwiOjE0NzA5ODI2MDAyMzksXCJhdWRpdFN0YXRlXCI6bnVsbCxcImN1cnJlbnRQb2ludFwiOjB9In0.i8jR9W4hHXf3AhwR3bVc4sG5MrFIwCZbnZ39c9cZQvqg754XJmcXpK6xoA92I_EKZcd2_t1J1npRk_qr5HXg-hjx5-Pfw5cks4EdU-bxZG4WL9AqtETp7RtUqy-8zt6Ek16baHjzSX0UfdjqBLErheHScoDH_B89VEZRBSH4XuzRWd7ClR-aQ0cMKWa2APsEmRlyE2lNQMDxjNsKLNmMqETgWxeu6wrX8Fe8n0P3IFHbTc61mMPai5s_vMw4HCobFrJmlWrRGtCMPeru2aMqsN1C1Qu3-1MXr26Ezx5HOWpSwrxgnHaBZdRADCntVrxEjRrPBeTZBJ-cPstPPGGUjA",
    "Authorization": "Bearer eyJraWQiOiJhMTE3ZTA5Ny1jNWJiLTRmZTQtYTMwMC00MjE4NWI4MGY2MDYiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpc3N1ZXIiLCJhdWQiOiJhdWRpZW5jZSIsImV4cCI6MTQ3MDk4MjYwMCwianRpIjoieE1aNXBZY3lQNkE3YWdLQkt5eENfZyIsImlhdCI6MTQ3MDQyNjAzMywibmJmIjoxNDcwNDI1OTEzLCJzdWIiOiIxODk4ODk5MjQ5MiIsImF0dHJpYnV0ZXMiOiJ7XCJhZGRyZXNzXCI6bnVsbCxcInN1cHBsaWVySWRcIjpudWxsLFwic3VwcGxpZXJcIjpudWxsLFwibG9naW5QYXNzd29yZFwiOm51bGwsXCJtb2JpbGVcIjpcIjE4OTg4OTkyNDkyXCIsXCJuYW1lXCI6XCLlp5pcIixcInZhbGlkYXRlQ29kZVwiOlwiOTA0NFwiLFwiaWRcIjpcIjU3MjA0YjgyMGNmMmZmMjExNDkzYjllOVwiLFwiJGV4cGlyYXRpb24tdGltZVwiOjE0NzA5ODI2MDAyMzksXCJhdWRpdFN0YXRlXCI6bnVsbCxcImN1cnJlbnRQb2ludFwiOjB9In0.v-nLA9r8RLL0rZVZG4Ja6cmEWrWZ0fL3Dxvhw63tjLLDzCGS-2D8Uh3oldt_Na1zuKlwr3F5dgzqakgCpAQ3DrUBZjOtA_1SR8bFQ4MYRfCoVl5KSupaUN4kwKOTM1IKUCKfuWa5w8KeEL7AcDT_QxNU11F3OARX379VhKv-RcLffTk3PenbIqXu48_T96SaurDwFNYq741J5Zp_40bzGXSUVddM5wAWd0Afxt4rohJWoJnUXl6mzHHv9tiLVLuIc1pHGiXzdHi4JW51TV65T5axTohKlAFHNiWxG10TQ9O4YBUUXkRuHXajmJuTsLJ3KRvUgC7q_bEU4c0dZIxU5Q",
    "Origin": "file://"
}


def get_list_params(page_number=1):
    return [{"id": 'id' + str(random.randint(1000000000, 9999999999)),
             "name": "supplierWebRpc.fullTextSearchSuppliers",
             "args": ["{\"auditState\":\"Authenticated\",\"key\":\"\"}", "{\"page\":%s,\"size\":50}" % page_number]}]


def get_mobile_params(supplier_id):
    return [{"id": "id9247007885", "name": "supplierWebRpc.showSupplierMobile",
             "args": ["\"56c7d4ac7c1f5d3b683c709c\"", "\"12345678901\""]}]


filename = '..\supplier_list.json'
file = open(filename, 'wb')

for page_number in range(0, 34):
    print "reading page %d" % page_number
    r = requests.post(url, json=get_list_params(page_number), headers=headers)
    file.write(r.content)
    file.write('\n')
    print "[%s] %s" % (r.status_code, r.content)

file.close()

# mobile_info = requests.post(url, json=get_mobile_params('56c7d4ac7c1f5d3b683c7097'), headers=headers)
# print mobile_info.content
