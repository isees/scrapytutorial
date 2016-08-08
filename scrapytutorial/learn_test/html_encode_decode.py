# -*- coding: utf-8 -*-

import urllib


def decode(url):
    return urllib.unquote(url).decode('utf8')

# 订一束
url = "http%3A%2F%2Fwww.easyflower.com%2Fdingyue%2Fflower%2Fproduct%2Fdetail.do?id=52700&showwxpaytitle=1&response_type=code&scope=snsapi_userinfo&state=1234#wechat_redirect"
print decode(url)

url2 = "http%3A%2F%2Fwww.easyflower.com%2Fdingyue%2Fflower%2ForderConfirm.do?data={%22productId%22:100001,%22recommendId%22:0,%22specId%22:1000,%22gift%22:%22%E5%8C%A0%E4%BD%9C%E8%8A%B1%E5%99%A8%EF%BC%88%E9%A6%96%E6%AC%A1%E8%AE%A2%E9%98%85%E4%B8%93%E4%BA%AB%E7%A6%8F%E5%88%A9%EF%BC%89%22}&showwxpaytitle=1&response_type=code&scope=snsapi_userinfo&state=1234&connect_redirect=1#wechat_redirect"
print decode(url2)

# 随心阅
url3 = "http%3A%2F%2Fwww.easyflower.com%2Fdingyue%2Fflower%2Fproduct%2Fdetail.do?id=100001&showwxpaytitle=1&response_type=code&scope=snsapi_userinfo&state=1234#wechat_redirect"
print decode(url3)

# 社区
url4 = "http%3A%2F%2Fwap.webei.cn%2F5c07644699%2FwxLogin&response_type=code&scope=snsapi_userinfo&state=km49q1467624929&connect_redirect=1#wechat_redirect"
print decode(url4)

# 往期花束 | 随心阅
url5 = "http://mp.weixin.qq.com/s?__biz=MzAxMTEyMzUwNg==&mid=403427679&idx=1&sn=42664b3ae0b97ce39647dbd9f448e77d&scene=1&srcid=070418SrPZqWr2Nhsu9HMlVM#rd"
print decode(url5)

# 花颂首页
url_huasong = "https://wap.koudaitong.com/v2/showcase/homepage?kdt_id=14855821&reft=1469377615619&spm=f36760169&sf=wx_sm"
print decode(url_huasong)

# 花+混合花束
url_flowerplus = "http://mp.weixin.qq.com/mp/homepage?__biz=MzA3MzUxNzcyOQ==&hid=4&sn=567711fb7ed08d0c5249d93b74a1be48&uin=MTYzODU5NDY2Mw%3D%3D&key=77421cf58af4a6539668e8915df699335e17b14d7604d4b8b1d41b106c9c316990d491dd411d92e1c80f932e110fc412&devicetype=android-23&version=2603163c&lang=en&nettype=WIFI&pass_ticket=NrTmC5QQok9DoGm9PgJT6FDZkWjm1qIIr1bFA0A5dLlSKThhdPZFA9%2BIaYTLyamf&scene=1"
print decode(url_flowerplus)