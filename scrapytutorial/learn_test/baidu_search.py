# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

search_list_url = "https://www.baidu.com/s?ie=utf-8&mod=11&isbd=1&isid=d40e01ef00014e94&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%B1%B1%E5%9C%B0%E8%BD%A6%20%E9%AA%91%E8%A1%8C&oq=%E6%B5%8B%E8%AF%95&rsv_pq=d40e01ef00014e94&rsv_t=d572WSqnwzErF4Vhplk%2B5xcVawDM2r7E8bV3vWsX1yn33RXbC8Qs%2FPKYdH4&rqlang=cn&rsv_enter=1&inputT=31041&rsv_sug3=32&rsv_sug1=28&rsv_sug7=100&sug=%E6%B5%8B%E8%AF%95%E7%BD%91%E9%80%9F&rsv_n=1&bs=%E6%B5%8B%E8%AF%95&rsv_sid=1420_18280_18560_17001_11655_20856_20733_20837&_ss=1&clist=ebb9fcd0c2248c24%0997f575a8550eb378&hsug=&csor=6&pstg=5&_cr1=38172"

headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8,ar;q=0.6",
    "Cache-Control": "no-cache",
    "Host": "www.baidu.com",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Cookie": "BAIDUID=8D27927E1211A6FD34BE0D6F2A4C1630:FG=1; PSTM=1467911842; BIDUPSID=2726F935573AC522580E279FCAF6B311; sugstore=1; pgv_pvi=8610781184; ispeed_lsm=0; BD_HOME=0; BD_UPN=12314753; H_PS_645EC=d572WSqnwzErF4Vhplk%2B5xcVawDM2r7E8bV3vWsX1yn33RXbC8Qs%2FPKYdH4; BD_CK_SAM=1; BDSVRTM=17; H_PS_PSSID=1420_18280_18560_17001_11655_20856_20733_20837; __bsi=17440691342695070569_00_0_I_R_19_0303_C02F_N_I_I_0"

}

result = requests.get(search_list_url, headers=headers)
html = result.content
soup = BeautifulSoup(html, 'html.parser')
print soup
