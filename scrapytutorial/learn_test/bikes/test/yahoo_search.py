# coding: utf-8

import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080',
}

keyword = 'mountainbike'
url = 'https://search.yahoo.com/search?p=%s' % keyword
#
# headers = {
#     # ":authority": "www.google.com",
#     # ":method": "GET",
#     # ":path": "/",
#     # ":scheme": "https",
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "accept-encoding": "gzip, deflate, sdch, br",
#     "accept-language": "en-US,en;q=0.8,ar;q=0.6",
#     "cache-control": "no-cache",
#     "cookie": "SID=mgPyLwHqNVc26wVh7BCsYv-utj2827T-OLK-gczqUxco9xyBKx9QbF4hgFL1jU9feWWKAQ.; HSID=AXWwWt104XCG2rrHc; SSID=AflSPn01Un_ewxu5v; APISID=d_Kb8vD3ExU3wdI3/A4I--kT1DGrXgCp-Z; SAPISID=iIUp5-RTYTc5OwXk/ADrDveq_tjzx1tpVL; NID=85=aN4GO3FmZobk8wIJDzSkcRPN0vA0mdcTr_ke7zOB_EQNyfvX48mOvtMlDfEehJd4Z0Z989RfUvzrZVhaAlYwzICm-dc-nBaSEVcR2--0uhB57GOYYjeViF2xlfs-7e1LiolxBzLM2IOzbqpAqMYdFRU0oRjj_ng_XlHFfw6OVDKl7x2wJQxPjjSl2XcF-YCspaj9UfQYtDg2VcIUMFjGcSvMB2SyMVGUP6bo0U-DqkptzSiuuruxsliCh8CRA6sk3lfpK8XiKe0s_4y25FA; DV=svtiVQKpSEVDaq_t7ni56YkCYWfArRpDGylDv9ZDbAAAAFjmBgPHhfA9KAAAgLC1jdcPC7L3CgAAAA",
#     "pragma": "no-cache",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
# }

response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find("div", id='web').find_all("li").find_all("div", class_='compTitle')
# print soup.find("div", id='web').prettify()
for li in results:
    title = li
    # url = li.find("div", class_="compTitle").a.get("href")
    # abstract = li.find("div", class_="aAbs").text
    print title
    # print url
    # print abstract
    print '\n'



# for history in response.history:
#     print history.url, history.status_code, history.content
