# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_response(search_url):
    try:
        response = requests.get(search_url)
        return response
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        return None


def get_hot_list(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    main_body = soup.find(class_='mainBody')
    hot_person_list = []
    if main_body is not None:
        i = 0
        for group in main_body.find_all("a", class_="list-title"):
            if i > 10:
                break
            i += 1
            name = group.text.strip()
            if name not in hot_person_list:
                hot_person_list.append(name)
    return hot_person_list


def get_hot_start_list():
    hot_person = 'http://top.baidu.com/buzz?b=258'
    hot_fun = 'http://top.baidu.com/buzz?b=618'

    person_list = get_hot_list(hot_person)
    fun_list = get_hot_list(hot_fun)

    return list(set(person_list + fun_list))
