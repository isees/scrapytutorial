# coding: utf-8

import scrapy_data as sd
import requests
from bs4 import BeautifulSoup
import hashlib

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080',
}


def search_and_save():
    keywords = sd.get_keyword_list('D:\workspace\python\scrapytutorial\doc\soogic\en_keywords')
    hot_words = sd.get_keyword_list('D:\workspace\python\scrapytutorial\doc\soogic\en_hotwords')
    for hot_word in hot_words:
        for keyword in keywords:
            save_data(keyword, hot_word)


def search_data(search_word):
    url = 'https://search.yahoo.com/search?p=%s' % search_word
    response = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def save_data(keyword, hot_word):
    soup = search_data(keyword + " " + hot_word)
    results = soup.find("div", id='web').find_all("li")
    url_md5_list = sd.get_all_url_md5()

    for li in results:
        try:
            a = li.find("div", class_="compTitle").a
            title = a.text.strip()
            url = a.get("href")
            abstract = li.find("div", class_="aAbs").text
            title_md5 = hashlib.md5(title.encode('utf-8')).hexdigest()

            if title_md5 in url_md5_list:
                print '<<%s>> exists' % title
                continue
            url_md5_list.append(title_md5)

            url_md5 = hashlib.md5(url.encode('utf-8')).hexdigest()
            if url_md5 in url_md5_list:
                print '"%s" exists' % url
                continue
            url_md5_list.append(url_md5)

            print title, ' [%s %s] - %s' % (keyword, hot_word, sd.source_dict[2])
            print abstract
            print url
            print '\n'

            sd.save(url_md5, title_md5, title, abstract, url, keyword, hot_word, 0, 2)
        except Exception:
            continue
