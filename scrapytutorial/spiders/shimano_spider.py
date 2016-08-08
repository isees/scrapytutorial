# import requests
#
# official_site = "http://www.shimano-china.com"
# prefix = ".quickview.json"
#
#
# # detail_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000/sl-m9000.quickview.json"
#
# def group_quickview_url(data_id):
#     return official_site + data_id + prefix
#
#
# def get_data_id_list(url):
#     pass
#
#
# product_list_url = "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000.html"
#
# headers = {
#     # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     # "Accept-Encoding": "gzip, deflate, sdch",
#     # "Accept-Language": "en-US,en;q=0.8,ar;q=0.6",
#     # "Cache-Control": "no-cache",
#     # "Host": "www.shimano-china.com",
#     # "Pragma": "no-cache",
#     # "Proxy-Connection": "keep-alive",
#     # "Upgrade-Insecure-Requests": "1",
#     # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch",
#     "Accept-Language": "en-US,en;q=0.8,ar;q=0.6",
#     "Cache-Control": "no-cache",
#     "Cookie": "Hm_lvt_2c2cb440510b4247aaffb935ef59ce7e=1470457994,1470460208; Hm_lpvt_2c2cb440510b4247aaffb935ef59ce7e=1470461927",
#     "Host": "www.shimano-china.com",
#     "Pragma": "no-cache",
#     "Proxy-Connection": "keep-alive",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
# }
#
# proxies = {
#     "http": "http://127.0.0.1:1080"
# }
# result = requests.post(product_list_url, headers=headers)
# print result.content
# # print result.cookies
# # print result.headers
#
# # div id = productFillArea
# # td data-id


# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ShimanoSpider(scrapy.Spider):
    name = "shimano"
    allowed_domains = ["www.shimano-china.com"]
    start_urls = [
        "http://www.shimano-china.com/content/sssc-bike/zh/home/components1/mountain/xtr-m9000.html"
    ]


    def parse(self, response):
        # filename = response.url.split("//")[1].split("/")[0] + '.txt'
        html = Selector(response=response).xpath('//body/text()').extract()
        print html
        # html = Selector(response=response).extract()
        # print html

        # f = open(filename, 'wb')
        # for line in html:
        #     if line.strip() == '':
        #         continue
        #     href = Selector(text=line).xpath('//a//@href').extract()
        #     title = Selector(text=line).xpath('//h2[re:test(@class, "title")]/text()').extract()
        #     img = Selector(text=line).xpath('//img[re:test(@class, "img")]//@src').extract()
        #     f.write(title.pop() + '\n')
        #     f.write(href.pop() + '\n')
        #     f.write(img.pop() + '\n')
        #     f.write('\n')
        #     f.write('\n')
        # f.close()
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
