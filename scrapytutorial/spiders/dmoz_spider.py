# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
        "http://yibugou.com.cn/",
        "http://www.oschina.net/search?scope=blog&q=UnicodeEncodeError",
        "http://www.jb51.net/article/17560.htm"
    ]

    def parse(self, response):
        filename = response.url.split("//")[1].split("/")[0] + '.txt'
        html = Selector(response=response).xpath('//span/text()').extract()
        # print html
        f = open(filename, 'w')
        for line in html:
            if line.strip() == '':
                continue
            f.write(line + '\n')
        f.close()
        # with open(filename, 'wb') as f:
        #     for line in html:
        #         print '%s wrote' % line
        #         f.write(line)
