# -*- coding: utf-8 -*-
import json
import requests
import sys
from bs4 import BeautifulSoup
import ast

reload(sys)
sys.setdefaultencoding('utf-8')

official_site = "http://www.shimano-china.com"
official_site_en = "http://www.shimano.com"
prefix = ".quickview.json"

page_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000.html"
series_json_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000/_jcr_content/results.updateresults.json?page=1"


# detail_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000/sl-m9000.quickview.json"

def group_quickview_url(data_id):
    return official_site + data_id + prefix


def get_data_id_list(url):
    pass


# product_list_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000.html"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8,ar;q=0.6",
    "Cache-Control": "no-cache",
    "Host": "www.shimano.com",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

headers_cn = {
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

proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "http://127.0.0.1:1080"
}


def get_if_exist(json, name):
    if json:
        for key in json.keys():
            if name in key:
                return json[key].strip()
    return ''


def split_array(text, label):
    list = []
    for line in text.split(label):
        if line.strip() is "":
            continue
        list.append(line.strip())
    return list


def save_series(product_list_url):
    result = requests.get(product_list_url, headers=headers)
    html = result.content
    soup = BeautifulSoup(html, 'html.parser')

    product_container = soup.find(id="productFillArea")
    for line in product_container.find_all("td", class_="product"):
        data_id = line['data-id']
        json_info_url = official_site_en + data_id + prefix
        response = requests.get(json_info_url, headers=headers)
        json_info = response.content
        try:

            info = json.loads(json_info, encoding='utf-8')

            id = info['id']
            name = info['name']
            model = get_if_exist(info['attributes'], '型号')
            series = get_if_exist(info['attributes'], '系列')
            image_url = info['image'].split('.swimg')[0]
            specific_url = info['url']
            features = ast.literal_eval(json.dumps(info['features'], ensure_ascii=False))

            attributes = json.dumps(info['attributes'], ensure_ascii=False)
            technology = json.dumps(info['technology'], ensure_ascii=False)

            print 'name>> %s' % name
            print 'model>> %s' % model
            print 'series>> %s' % series
            print 'image_url>> %s' % (official_site_en + image_url)
            print 'specific_url>> %s ' % (official_site_en + specific_url)
            feature_list = split_array(features[0], "•")
            # for feature in json.dumps(feature_list, ensure_ascii=False).split("\n"):
            #     if feature.strip() is not '':
            #         feature_list.append(feature.strip())
            print 'features>> %s' % json.dumps(feature_list, ensure_ascii=False)
            print 'attributes>> %s' % attributes

            print '\n'
        except Exception, err:
            print '0 #############################################################'
            print err.message
            print json_info_url
            print response
            print json_info
            print '1 #############################################################'
            continue


url_list = [
    "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/road/_.html",
    "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000.html"
]


def save_url_list(url_list):
    for product_list_url in url_list:
        save_series(product_list_url)


def html_url_to_json_url(html_url, page=1):
    new_url = official_site_en + html_url.replace(".html", "/_jcr_content/results.updateresults.json")
    if page > 1:
        new_url += "?page=%d" % page
    return new_url


def get_series_url_list(url):
    result = requests.get(url, headers=headers_cn, proxies=proxies)
    soup = BeautifulSoup(result.content, 'html.parser')
    product_container = soup.find("div", id="top-nav").find("ul", class_="product_categories")
    series_list = product_container.find_all("li", recursive=False)
    category = {}
    for series in series_list:
        series_title = series.a.text.strip()
        series_product_list = series.ul.find_all("a")
        print series_title
        product = {}
        for product in series_product_list:
            product[product.text.strip()] = html_url_to_json_url(product.get("href"))
        category[series_title] = product
        print product.text, html_url_to_json_url(product.get("href"))
        print "\n"  # TODO: mask
        # save_url_list(url_list)
    print json.dumps(category, ensure_ascii=False)

# TODO: Get all url list
get_series_url_list(official_site)
