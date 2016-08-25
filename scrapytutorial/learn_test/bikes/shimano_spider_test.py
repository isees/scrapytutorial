# -*- coding: utf-8 -*-
import json
import requests
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

official_site = "http://www.shimano-china.com"
prefix = ".quickview.json"


# detail_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000/sl-m9000.quickview.json"

def group_quickview_url(data_id):
    return official_site + data_id + prefix


def get_data_id_list(url):
    pass


product_list_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000.html"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8,ar;q=0.6",
    "Cache-Control": "no-cache",
    "Host": "www.shimano-china.com",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

result = requests.get(product_list_url, headers=headers)
html = result.content
soup = BeautifulSoup(html, 'html.parser')

product_container = soup.find(id="productFillArea")
for line in product_container.find_all("td", class_="product"):
    data_id = line['data-id']

    json_info_url = official_site + data_id + prefix
    print json_info_url

    json_info = requests.get(json_info_url, headers=headers).content
    info = json.loads(json_info)

    print info['id']
    print info['name']
    print info['image'].split('.swimg')[0]
    # print info['technology']
    # print info['description']
    print info['url']
    print 'features: '
    if len(info['features']) > 1:
        print '#########################'
    # for element in info['features']:
    #     print element
    print json.dumps(info['features'], ensure_ascii=False)
    print json.dumps(info['attributes'], ensure_ascii=False, encoding='utf-8')
    # for key, value in info['attributes'].items():
    #     print key+":"+value

    print '\n'
