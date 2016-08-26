# -*- coding: utf-8 -*-

import requests

search_url = 'http://www.baidu.com/link?url=i5HrX_2799XTKcjEvo6taKz5HfpkFLyhw__RR9bGbn_sqtN-e88sDQPddiljHV3h'
response = requests.get(search_url)
if response.history:
    print "Request was redirected"
    for resp in response.history:
        print resp.status_code, resp.url
    print "Final destination:"
    print response.status_code, response.url
else:
    print "Request was not redirected"
