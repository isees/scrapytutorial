# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class FlowerSpider(scrapy.Spider):
    name = "flowerplus"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = [
        "http://mp.weixin.qq.com/mp/homepage?__biz=MzA3MzUxNzcyOQ==&hid=4&sn=567711fb7ed08d0c5249d93b74a1be48&uin=MTYzODU5NDY2Mw==&key=77421cf58af4a6539668e8915df699335e17b14d7604d4b8b1d41b106c9c316990d491dd411d92e1c80f932e110fc412&devicetype=android-23&version=2603163c&lang=en&nettype=WIFI&pass_ticket=NrTmC5QQok9DoGm9PgJT6FDZkWjm1qIIr1bFA0A5dLlSKThhdPZFA9+IaYTLyamf&scene=1"
        # "http://mp.weixin.qq.com/s?__biz=MzA3MzUxNzcyOQ==&amp;mid=508541369&amp;idx=1&amp;sn=ff94fd56ed914f38a61ff5cc6cdcb1b2&amp;scene=19#wechat_redirect"
    ]

    page_url = "http://mp.weixin.qq.com/mp/homepage?__biz=MzA3MzUxNzcyOQ==&hid=4&sn=567711fb7ed08d0c5249d93b74a1be48&uin=MTYzODU5NDY2Mw==&key=77421cf58af4a6539668e8915df699335e17b14d7604d4b8b1d41b106c9c316990d491dd411d92e1c80f932e110fc412&devicetype=android-23&version=2603163c&lang=en&nettype=WIFI&pass_ticket=NrTmC5QQok9DoGm9PgJT6FDZkWjm1qIIr1bFA0A5dLlSKThhdPZFA9+IaYTLyamf&scene=1&cid=0&cid=0&begin=5&count=5&action=appmsg_list&f=json"

    def parse(self, response):
        filename = response.url.split("//")[1].split("/")[0] + '.txt'
        html = Selector(response=response).xpath('//a[re:test(@class, "list_item")]').extract()
        f = open(filename, 'wb')
        for line in html:
            if line.strip() == '':
                continue
            href = Selector(text=line).xpath('//a//@href').extract()
            title = Selector(text=line).xpath('//h2[re:test(@class, "title")]/text()').extract()
            img = Selector(text=line).xpath('//img[re:test(@class, "img")]//@src').extract()
            f.write(title.pop() + '\n')
            f.write(href.pop() + '\n')
            f.write(img.pop() + '\n')
            f.write('\n')
            f.write('\n')
        f.close()
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
