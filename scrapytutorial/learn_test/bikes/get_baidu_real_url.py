# -*- coding: utf-8 -*-

import requests

headers = {
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Host": "www.baidu.com"
}

search_url = 'http://www.baidu.com/link?url=uNdUduz8zdqoNk2j97A5yJ7SBTppDXJd8P5XxylPe9ssxel9hn1GnhqMzt08WjyKKp56Z7Typyv7vJOdLIFNq-I_nDKqPyH8wNic9Hb1mCi'
response = requests.get(search_url)
if response.history:
    print "Request was redirected"
    for resp in response.history:
        print resp.status_code, resp.url
    print "Final destination:"
    print response.status_code, response.url
else:
    print "Request was not redirected"
